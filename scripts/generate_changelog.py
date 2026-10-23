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
    sections = split_sections(text)
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
            if last:
                try:
                    log = git("log", "--oneline", f"{last}..{head}", cwd=dest)
                except subprocess.CalledProcessError:   # force-push / rewritten history
                    log = git("log", "--oneline", "-n", "20", cwd=dest)
            elif fallback:
                log = git("log", "--oneline", f"--since={fallback}T00:00:00Z", cwd=dest)
            else:
                log = git("log", "--oneline", "--since=24 hours ago", cwd=dest)
            new_state[repo] = head
            if log:
                new[repo] = [f"- {l}" for l in log.splitlines()]

    if not new:
        STATE.write_text(json.dumps(new_state, indent=2) + "\n")
        print("No new commits.")
        return

    # Merge into today's section (new commits on top) or create it.
    if sections and sections[0][0] == today:
        data = parse_body(sections[0][1])
        rest = sections[1:]
    else:
        data, rest = {}, sections
    for repo, lines in new.items():
        data[repo] = lines + [l for l in data.get(repo, []) if l not in lines]

    blocks = [render(today, data)] + [f"## {d}\n\n{b}" for d, b in rest]
    OUT.write_text(TITLE + "\n\n" + "\n\n".join(blocks).rstrip() + "\n")
    STATE.write_text(json.dumps(new_state, indent=2) + "\n")
    print("Updated:", ", ".join(new))


if __name__ == "__main__":
    sys.exit(main())
