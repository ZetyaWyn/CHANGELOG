#!/usr/bin/env python3
"""Update CHANGELOG.md with new commits, tracking the last-seen SHA per repo."""
import json, re, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

ORG = "project-sm7435"
REPOS = [
    "device_xiaomi_garnet",
    "vendor_xiaomi_garnet",
    "device_xiaomi_garnet-miuicamera",
    "vendor_xiaomi_garnet-miuicamera",
    "hardware_dolby",
]
KERNEL = [
    ("android_kernel_xiaomi_sm7435", "16.2"),
]
MODULES = [
    ("android_kernel_xiaomi_sm7435-modules", "lineage-23.2"),
]

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "CHANGELOG.md"
STATE = ROOT / ".last_shas.json"
TITLE = "# Changelog"


def git(*args, cwd=None):
    return subprocess.run(["git", *args], cwd=cwd, check=True,
                          capture_output=True, text=True).stdout.strip()


def split_sections(text):
    """Return list of (date, body) in file order."""
    parts = re.split(r"(?m)^## (\d{4}-\d{2}-\d{2})\s*$", text)
    return [(parts[i], parts[i + 1].strip("\n")) for i in range(1, len(parts), 2)]


def parse_body(body):
    """body -> {repo: [bullet lines]} (only commit repos)."""
    data, cur = {}, None
    for line in body.splitlines():
        m = re.match(r"### (\S+)", line)
        if m:
            cur = m.group(1)
            data.setdefault(cur, [])
        elif cur and line.startswith("- ") and line != "- No new commits.":
            if not line.startswith("- ["):
                data[cur].append(line)
    return data


BULLET = re.compile(r"^- ([0-9a-f]{7,40}) (.*)$")


def sha_seen(sha, known):
    """Abbreviated SHAs can change length as a repo grows, so match by prefix."""
    return any(k.startswith(sha) or sha.startswith(k) for k in known)


def merge_duplicate_dates(sections):
    """Collapse repeated '## date' headings into one section, dropping repeated SHAs."""
    order, bodies = [], {}
    for d, b in sections:
        if d not in bodies:
            order.append(d)
        bodies.setdefault(d, []).append(b)
    merged = []
    for d in order:
        if len(bodies[d]) == 1:
            merged.append((d, bodies[d][0]))
            continue
        data, seen = {}, set()
        for b in bodies[d]:
            for repo, lines in parse_body(b).items():
                for l in lines:
                    m = BULLET.match(l)
                    key = m.group(1) if m else l
                    if not sha_seen(key, seen):
                        seen.add(key)
                        data.setdefault(repo, []).append(l)
        merged.append((d, render(d, data).split("\n", 2)[2].strip("\n")))
    return merged


def check(text):
    """Return a list of problems: duplicate date headings or duplicate SHAs."""
    problems = []
    dates = re.findall(r"(?m)^## (\d{4}-\d{2}-\d{2})\s*$", text)
    problems += [f"duplicate section: {d}" for d in sorted({d for d in dates if dates.count(d) > 1})]
    shas = [m.group(1) for l in text.splitlines() if (m := BULLET.match(l))]
    seen = []
    for sha in shas:
        if sha_seen(sha, seen):
            problems.append(f"duplicate commit: {sha}")
        seen.append(sha)
    subjects = set()
    for d, body in split_sections(text):
        for repo, lines in parse_body(body).items():
            for l in lines:
                m = BULLET.match(l)
                if m and (repo, m.group(2)) in subjects:
                    problems.append(f"duplicate message in {repo}: {m.group(2)}")
                elif m:
                    subjects.add((repo, m.group(2)))
    return problems


def dedupe(secs):
    """secs: [(date, {repo: [bullets]})] newest first. Keep the first (newest)
    occurrence of each commit message per repo; drop older repeats. Returns count removed."""
    seen, removed = set(), 0
    for _, data in secs:
        for repo, lines in data.items():
            kept = []
            for l in lines:
                m = BULLET.match(l)
                key = (repo, m.group(2)) if m else None
                if key and key in seen:
                    removed += 1
                    continue
                if key:
                    seen.add(key)
                kept.append(l)
            data[repo] = kept
    return removed


def write_all(secs):
    OUT.write_text(TITLE + "\n\n" + "\n\n".join(render(d, x) for d, x in secs).rstrip() + "\n")


def render(date, data):
    out = [f"## {date}", ""]
    for repo in REPOS:
        out += [f"### {repo}", ""]
        out += data.get(repo) or ["- No new commits."]
        out.append("")
    for heading, items in (("Kernel", KERNEL), ("Kernel Modules", MODULES)):
        out += [f"### {heading}", ""]
        for name, branch in items:
            out.append(f"- [{name}](https://github.com/{ORG}/{name}/commits/{branch}/)")
        out.append("")
    return "\n".join(out)


def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    text = OUT.read_text() if OUT.exists() else ""
    if "--check" in sys.argv:
        problems = check(text)
        print("\n".join(problems) if problems else "CHANGELOG OK: no duplicates.")
        return 1 if problems else 0
    sections = merge_duplicate_dates(split_sections(text))
    sections.sort(key=lambda x: x[0], reverse=True)          # newest first

    if "--clean" in sys.argv:                                 # offline cleanup of existing file
        secs = [(d, parse_body(b)) for d, b in sections]
        removed = dedupe(secs)
        write_all(secs)
        print(f"Removed {removed} duplicate entries.")
        return 0

    # Everything already written anywhere in the file, so nothing is listed twice.
    known_shas, known_subjects = [], {}
    for _, body in sections:
        for repo, lines in parse_body(body).items():
            for l in lines:
                m = BULLET.match(l)
                if m:
                    known_shas.append(m.group(1))
                    known_subjects.setdefault(repo, set()).add(m.group(2))
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    # Fallback window for repos with no saved SHA yet: since latest changelog date.
    fallback = sections[0][0] if sections else None

    new, new_state = {}, dict(state)
    with tempfile.TemporaryDirectory() as tmp:
        for repo in REPOS:
            dest = f"{tmp}/{repo}"
            git("clone", "--quiet", "--bare", "--single-branch", "--filter=blob:none",
                f"https://github.com/{ORG}/{repo}", dest)
            head = git("rev-parse", "HEAD", cwd=dest)
            last = state.get(repo)
            if last == head:
                continue
            exact = True    # True: SHA range is authoritative
            if last:
                try:
                    log = git("log", "--oneline", f"{last}..{head}", cwd=dest)
                except subprocess.CalledProcessError:   # force-push / rewritten history
                    log, exact = git("log", "--oneline", "-n", "20", cwd=dest), False
            elif fallback:
                log, exact = git("log", "--oneline", f"--since={fallback}T00:00:00Z", cwd=dest), False
            else:
                log, exact = git("log", "--oneline", "--since=24 hours ago", cwd=dest), False
            new_state[repo] = head
            lines = []
            for l in log.splitlines():
                sha, _, subject = l.partition(" ")
                if sha_seen(sha, known_shas):
                    continue                      # already in the changelog
                if not exact and subject in known_subjects.get(repo, ()):
                    continue                      # rebased copy of a listed commit
                lines.append(f"- {l}")
            if lines:
                new[repo] = lines

    secs = [(d, parse_body(b)) for d, b in sections]
    if new:
        if secs and secs[0][0] == today:
            data = secs[0][1]
        else:
            data = {}
            secs.insert(0, (today, data))
        for repo, lines in new.items():
            data[repo] = lines + [l for l in data.get(repo, []) if l not in lines]
    removed = dedupe(secs)

    if not new and not removed and not check(text):
        STATE.write_text(json.dumps(new_state, indent=2) + "\n")
        print("No new commits.")
        return 0

    write_all(secs)
    problems = check(OUT.read_text())
    STATE.write_text(json.dumps(new_state, indent=2) + "\n")
    if problems:
        print("Duplicates remain:\n" + "\n".join(problems))
        return 1
    print("Updated:", ", ".join(new) or "none", f"| removed {removed} duplicates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
    
