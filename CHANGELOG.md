# Changelog

## 2026-11-11

### device_xiaomi_garnet

- 0b510c1 garnet: Remove unused CoreSight modules

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- 64f8b32 dolby: new Atmos card with animated ring
- bce0517 dolby: add ViPER bass and clarity modes
- 21fbdc2 dolby: model ViPER bass and clarity effects on the GEQ
- c2b8e63 dolby: uwu

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-10

### device_xiaomi_garnet

- 3f569ce garnet: Enable R8 optimizations for system_server and SystemUI
- d260e0e garnet: Prefer HW codecs for video thumbnails
- ebd0842 garnet: Drop add_power_save (already set in vendor) and silence noisy log tags
- d619524 garnet: Add missing RKPD props from stock rom

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- ce1690e dolby: Fix master toggle reactivation and synchronize QS tile state

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-09

### device_xiaomi_garnet

- 2d41f87 garnet: charging: 36C -> 5, 38C -> 10, 40C -> 16

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-08

### device_xiaomi_garnet

- 1db77d3 garnet: overlay: enable WFC by default
- 7b5495e garnet: sepolicy: allow system_app to read battery temp
- 8d434a1 garnet: props: remove debug.sf.enable_adpf_cpu_hint
- e7de734 garnet: charging: 37C -> 5, 39C -> 10, 41C -> 16, hyst 1C
- 07aded8 garnet: charging: 40C -> 10, 43C -> 16
- ae60723 garnet: sepolicy: Add missing proc_vm type
- c38e9b6 garnet: init: grant Power HAL access to CPU scaling nodes
- 8b47e54 garnet: sepolicy: allow power HAL to access performance interfaces
- 23488de garnet: sepolicy: allow power HAL to access cpu_dma_latency
- 0b09ff0 garnet: sepolicy: Allow hal_power_default to read graphics sysfs
- 84cca23 garnet: Remove unnecessary dex2oat properties

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-07

### device_xiaomi_garnet

- 747136b garnet: Fix CPU scaling and configure kernel manager
- 67153ae garnet: properties: Enable VoLTE and VoWIFI for all carriers
- df9dfca garnet: overlay: Use 4G instead of LTE icon for save statusbar space
- cb159c3 garnet: Improve battery charging control with hysteresis
- 2503619 garnet: sepolicy: allow hal_audio_default to access miev and set vendor_audio_prop
- 7d27899 garnet: charging: fix label, temp units, charger perms
- 196a713 garnet: parts: Only override Dolby Vision HDR type
- 96ef0ee garnet: Drop qesdk blobs
- 830bcce garnet: Bump super size to fix gapps errors
- 759270b garnet: Remove Force triple frame buffers
- b2c734e garnet: Add props to improve battery backup
- f92efda garnet: Enable SurfaceFlinger's display power timer
- d88dbe0 garnet: Update from OS3.0.304.0.WNRMIXM
- 53d30af garnet: Update from OS3.0.302.0.WNRMIXM
- 6ba397a garnet: Remove lineage dependencies
- c273a2a garnet: Grant GPU sysfs access for kernel manager and diagnostics
- 8867b7f garnet: init: Read camera sensor for proper about phone camera description
- e9f1413 garnet: include axion common soc_map
- 952b258 garnet: Bring up Axion
- 09d8fb4 garnet: power: Rework powerhint and add FLING/UI_ANIMATION
- f7859b9 garnet: power: Set GPUMinFreq 650MHz & GPUMaxFreq 940MHz on EXPENSIVE_RENDERING
- 1ab3871 garnet: powerhint: Refine performance hints for various scenarios
- 3357314 garnet: Change to Arm64 Only
- e6112c4 [TMP] garnet: Disable PRODUCT_OTA_ENFORCE_VINTF_KERNEL_REQUIREMENTS
- 1231de8 garnet: Enable AOSP surfaceflinger
- d62f10d garnet: rootdir: Do not allow foreground tasks to run on CPU7
- 98364c6 garnet: rootdir: Move background cpuset to CPU0-1
- d453f8d garnet: rootdir: Set restricted cpuset to the same CPUs as system-background
- 9fc14dc garnet: overlay: Remove PowerProfile.POWER_NONE
- 89a76dd garnet: disable verbose camera logs
- b8ae429 garnet: Set sensors logging level to warn
- 98dfae7 garnet: Kill log spam in logcat from SensorService
- 4e80fa1 garnet: Silence some spammy logging
- 5288d8f garnet: Build some missing LDAC libs
- c2d8832 garnet: properties: Enable QCRIL radio power saving
- 205f155 garnet: props: Disable Logs
- fc5c54a garnet: Disable continuous transaction tracing on all build types
- 0060da1 garnet: Set display idle time to 0
- 3cd5968 garnet: enable common build flags
- e24fece garnet: Fix HBM sepolicy issues
- 041afbb garnet: init: Give thermal profiles permissions 05-01 19:34:36.590 W/binder:2826_4(2826): type=1400 audit(0.0:3287): avc:  denied  { write } for  name="sconfig" dev="sysfs" ino=65252 scontext=u:r:system_app:s0 tcontext=u:object_r:sysfs_thermal:s0 tclass=file permissive=0 05-01 19:34:36.594 W/FileUtils(2826): No such file /sys/class/thermal/thermal_message/sconfig for writing 05-01 19:34:36.594 W/FileUtils(2826): java.io.FileNotFoundException: /sys/class/thermal/thermal_message/sconfig: open failed: EACCES (Permission denied)
- 7f209fe garnet: Fix gamebar GPU info
- c40cb63 garnet: Drop bypass charging and update translations
- 9e6c5c1 garnet: parts: Enable predictive back gestures
- 06948a6 garnet: parts: Refine UI
- 1c066ac garnet: parts: Move GameBar strings to resources and translate
- 0aa3055 garnet: parts: Apply expressive design style
- c2ed026 garnet: parts: Add translations for pt-BR, pt-PT, hi, fr, de, it, ar, ja, ko, az, ca, ckb, el, en-rAU, en-rCA, en-rGB, en-rIN, fa, ga-rIE, hu, iw, nn-rNO, pl, ro, sl, sq, ta, ug and vi
- dba365d garnet: parts: Import from xiaomi_sdm845-common https://github.com/LineageOS/android_device_xiaomi_sdm845-common/tree/e261035d91b34cf0fdf0f012927e06a2bcdb03ed/parts
- 82f1737 garnet: Speed profile services and wifi-service to reduce RAM and storage
- bd96568 garnet: init: rm package cache on early boot
- e2c7fdb garnet: fstab: set readahead_size_kb=128 to data
- a98b8c4 garnet: rootdir: Set correct permission for ntsync
- 7b242b9 garnet: Load ntsync module at boot
- fd60c57 garnet: Add SM7435 init script
- bda984c garnet: fix off-mode charging trigger
- 12ae4c0 garnet: Add missing permission for charging
- f74d3e4 garnet: Drop permissive mode and label charging policy
- 200f0ee garnet: Implement thermal-based charging control
- 1ae310a garnet: Guard erofs hints for erofs build
- da6fb84 garnet: Add erofs compress hints
- 2085ee9 garnet: Build gapps by default
- a40c360 garnet: Switch system partitions to EROFS
- ec44955 garnet: rootdir: Use foreground cpuset/uclamp for gralloc Makes sure rendering has enough capacity.
- a931794 garnet: rootdir: Use foreground uclamp for hwcomposer Matches SF, makes sure rendering always has enough capacity.
- fca0438 garnet: debloat: Remove Pixel Live Wallpaper
- 00d3530 garnet: debloat: Drop jelly app
- 738a1c3 garnet: Include app debloater
- 45b27f7 garnet: Switch to 8GB Dalvik heap config
- 115bbc0 garnet: overlay: Set default pin amount for home app
- 565eae0 garnet: overlay: Add webview pinning
- a4dfa37 garnet: Remove duplicate heap growth limit
- 325c665 garnet: sepolicy: Neverallow app open access to /dev/ashmem
- e8dde40 garnet: Add unix to hide Magisk in banking apps
- f00023b garnet: init: Give proper permissions for /dev/diag
- 031a74c garnet: Disable QCOM system daemon
- cc9d499 garnet: rootdir: Remove IO read_ahead_kb tune
- e54d400 garnet: audio: Route spatial output to Bluetooth
- 32147d6 garnet: rootdir: Set swappiness to 60
- caffd66 garnet: rootdir: Don't configure zram in QCOM's init post boot script
- c5e7c24 garnet: camera: Set torch default strength level to max
- e00c33b garnet: Implement torch light control
- a1ccff8 garnet: Fixing connecting BLE (bt 5.x) devices (smart watches, etc.)
- c27ed81 garnet: audio: Add fallback SW A2DP routes
- 506491e garnet: Audio: Enable support of HW Accelerated Effects
- 2798af7 garnet: audio: Add hardware accelerated audio effect
- c7f4eb4 garnet: audio: Add DSEE effect
- f56e63d garnet: audio: Fix overly loud notification sound
- bec7344 garnet: Move c2_manifest_vendor.xml to device tree
- 7013d62 garnet: Import QCOM audio effects from OnePlus 9R
- a337c8f garnet: audio: use QCOM Implementation for Audio Effects
- f5cd4b6 garnet: Include Sony Dolby Atmos and Sync with Spatial Audio
- 556a787 garnet: props: Increase audio offload buffer size from 32KB to 64KB
- f8671f6 garnet: audio: Fix mic issues in apps like WhatsApp
- e82d01c garnet: DeviceAsWebcam: set HQ mode as default
- 28ffeaa garnet: DeviceAsWebcam: disable USAGE_VIDEO_ENCODE ImageReader flag
- e4778f5 garnet: Build DeviceAsWebcam service
- dafd5b3 garnet: Setup DeviceAsWebcam
- e8b6df7 garnet: Limit background CPU utilization
- a7f1e59 garnet: Limit dex2oat cpu utilization
- f468bf7 garnet: overlay: Enable PowerOffAlarmService
- db127c6 garnet: sepolicy: Allow PowerOffAlarm app to find alarm service
- 9beab7f garnet: rootdir: fix battery drain due to statsd
- a02c5f8 garnet: overlay: Improve auto brightness
- 571f370 garnet: Tweak some auto brightness configs
- 943755d garnet: Optimize auto brightness adjustment
- c70eed3 garnet: overlay: lower autoBrightness Debounce
- 255ccc7 garnet: overlay: Increase auto brightness debounce
- 5c6bd58 garnet: overlay: Add overlay to improve signal reception
- d4e291a garnet: overlay: Enable Smart 5G
- 3d732e8 garnet: overlay: Define OEM fast charge sysfs node
- fff712f garnet: overlay: Enable Smart Pixels
- b51a684 garnet: overlay: Disable high performance transitions
- ae03bb5 garnet: Decouple interactive state from display
- e27ecb6 garnet: Add SystemUI restart in restart advanced menu
- eb2bc25 garnet: Enable LTO Optimizations
- 1b7729b garnet: Overlay: Define config_screenRecorderAVCProfileLevel
- dc6582a garnet: wifi: Enable Optimized Power Management
- 5d6d1b3 garnet: wifi: Disable TDLS offchannel
- 4197460 garnet: wifi: Smarter decisions on whether to use a 2 or 5Ghz AP
- 84b2777 garnet: props: More VoNR props
- bce33cb garnet: Enable VoNR Calls support Change-Id: I3cc986fd2352dc266e0d423767192c15c3669c5b Signed-off-by: Omar Mohamed <omarcoptan9@gmail.com> Signed-off-by: Z E U S <iamdrzeus14@gmail.com>
- 1749bf2 garnet: Import carrier configuration from peridot
- b88e2e5 sm8250-common: overlay: Enable VoNR on Jio 5G
- 89d551c garnet: overlay: Set 5G threshold bandwidth to 0
- cce9466 sm8250-common: overlay: Only allow 5G SA on Jio
- 4de0126 garnet: overlay: Set LTE+ threshold bandwidth to 0
- 680d539 garnet: overlay: Globally enable LTE+ icon
- 2db9ca6 garnet: overlay: Allow VoLTE and VoWiFi by default
- f43d1e3 garnet: remove FRP lock
- fac5dd8 garnet: tune HWUI and SurfaceFlinger performance
- 99b0660 garnet: Enable frame pacing for smoother visual performance
- 9b84aa9 garnet: properties: Set persist.sys.purgeable_assets=1
- 97edbe8 garnet: Enable debug.performance.tuning
- abeea3c garnet: Apply dex2oat optimizations
- d185665 garnet: disable_gl_backpressure
- e1b3380 garnet: Set ro.netflix.bsp_rev
- ce765ae garnet: Disable EGL image tracking
- bb96b78 garnet: sepolicy: Label bluetooth props
- a999204 garnet: Enable TWS plus feature using persist property
- de8149f garnet: Enable Qualcomm TrueWireless™ Stereo
- b040f44 garnet: sepolicy: Allow fingerprint HAL to access performance and sensor nodes
- fc0bd3d garnet: Allow qti init shell to open/write page cluster size
- c61e516 garnet: sepolicy: Allow system_app to access zram sysfs nodes
- 621d8f9 garnet: sepolicy: Dontaudit camera hal default_prop
- b3d9fde garnet: properties: camera: enable aux camera access for all apps
- 8e734f6 garnet: sepolicy: Address system suspend denials
- e26d6a3 garnet: sepolicy: Allow init/vold to write storage sysfs parameters
- a2ee160 garnet: sepolicy: Label UFS discard_max_bytes
- b5be4d9 garnet: Set BOOT_SECURITY_PATCH
- ed650ea garnet: Set VENDOR_SECURITY_PATCH To PLATFORM
- c9be66e garnet: disable FW roaming when in idle mode When device is idle, disable FW roaming (LOW RSSI roam, high band roam) to save power
- ed9c2d8 garnet: overlay: Set Wi-Fi 6 support
- 38e8460 garnet: Add com.android.bluetooth context to seapp_contexts

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- eb716da garnet: Use foreground uclamp for Codec2 service
- 88ebadc dolby: init: Restore labels on persistent DMS data
- 49ccf2d dolby: init: Remove duplicate DMS directory creation
- 9b29644 dolby: sepolicy: Rework DMS access rules
- 93ed859 dolby: Import translations from Crowdin
- 8b2fe5d dolby: Merge LunarisDolby updates from Ghosuto
- 10502a7 dolby: Add missing library
- 253558a configs: Remove legacy OMX aliases from Dolby Codec2 decoders
- fb69b6a configs: Enable Dolby AC-4 decoding
- 9ae9366 dolby: update DAX and remove software codec
- 1e8d77a dolby: translation from Crowdin
- 768e7f4 dolby: show active audio output device on home screen
- f99912a dolby: Refine bass enhancement profiles
- 66b0e70 dolby: sync LunarisDolby updates
- 76ae9ce dolby: mark UDC/AC4 codecs as software-codec, enable AC4

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-06

### device_xiaomi_garnet

- 2bb23f4 garnet: Update CPU permissions and clean up sepolicy

### vendor_xiaomi_garnet

- e161684 garnet:Update OnePlus 9R audio effects libraries

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- 9e0173f dolby: Update Dolby and Qualcomm audio libraries

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-05

### device_xiaomi_garnet

- ea3be8a Remove unnecessary dex2oat properties

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-01

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- abb894e garnet: proprietary: Update thermal-normal.conf
- 8c1d494 garnet: proprietary: Update Adreno blobs to v@837.0.9

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-31

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-30

### device_xiaomi_garnet

- dbe737e sm8250-common: Grant GPU sysfs access for kernel manager and diagnostics
- 4bc6f18 garnet: sepolicy: Update vendor access rules
- 9e18b94 garnet: SEPolicy: Grant system_app access to thermal sysfs files

### vendor_xiaomi_garnet

- e0663c4 garnet: Update from OS3.0.304.0.WNRMIXM
- e6fa007 garnet: update shared_libs for greatwhite driver
- d013a75 garnet: Update shared libraries
- b6a97ce garnet: update GPU driver blobs from greatwhite V@0863.1
- 126fc18 garnet: Drop 32 Libs
- b25b8f7 garnet: Restore eUICC mirilhook from 35d1c0f
- 17ce437 garnet: init: Reset readahead values for 128 always
- af066d9 garnet: Don't configure zram in post boot scripts
- d5f9098 garnet: Import QCOM audio effects from OnePlus 9R
- 8846cb5 garnet: switch default I/O scheduler to mq-deadline
- 87e2aa2 garnet: Add missing Leica video filter
- 2844c10 garnet: switch to deep suspend-to-RAM
- 6e848fc garnet: Remove again QDESK and Qquard
- abcfc84 garnet: expand WALT game list and enable lib mask force
- 9c5525c garnet: Switch to LZ4KD
- 5a8e300 garnet: Add missing GPU firmware
- 2ff10e9 garnet: Add Dolby Media Codecs
- 41540a1 vendor: drop C2
- 09547dc garnet: tune scheduler, cpufreq and zram
- db3651e garnet: Update from OS3.0.302.0.WNRMIXM

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-29

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-28

### device_xiaomi_garnet

- 24664a0 garnet: opt into legacy UDFPS enroll UI
- 5faaaf0 garnet: Drop modemManager blobs
- 037a16e garnet: Drop qguard blobs
- 49f2e6c garnet: sepolicy: Label missing sysfs_wakeup nodes
- 0d6ddb2 garnet: sepolicy: Grant system_app access to hal_mlipay_hwservice
- 7402a44 garnet: overlay: Improve status bar visual consistency
- b38a44c garnet: overlay: Convert config_screenBrightnessDoze to float
- 8548c2c garnet: overlay: added AOD brightness sensor configuration
- dd68103 garnet: sepolicy: allow rild read default_prop
- bc18afc garnet: sepolicy: Allow system_server to write to audioserver_tmpfs
- 99eb17b garnet: sepolicy: Add sys_nice capability to hal_fingerprint_default
- f4676e2 garnet: sepolicy: Allow system_suspend to read sysfs_wakeup files
- 342a828 garnet: audio: Drop ultrasound-handset profile to fix route transitions
- d21b298 garnet: overlay: Show min/max refresh rate in settings
- 3f57727 garnet: overlay: Disable config show smooth display
- 2f93f88 garnet: Include MiuiCamera if exists
- 6392c5b garnet: sepolicy: Centralize all camera-related policies in device tree
- 5b3cb51 garnet: Wire up per fps sf durations
- 6499a1d garnet: Set base sf work durations duration props from stock
- 92f77f3 Revert "garnet: Update sf duration to 12.3ms"

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- 290553f dolby: Switch to compact navbar design
- f85fe5f Dolby: fix bass/EQ handling, snapshots and app profile monitor

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-27

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- 2bc1ef4 Dolby: restore original EQ/bass behavior, fix effect handling

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-26

### device_xiaomi_garnet

- 3cdfe2e garnet: Drop KProfile

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-24

### device_xiaomi_garnet

- 56c5e19 garnet: Update from OS3.0.301.0.WNRMIXM
- ccccb21 garnet: sepolicy: Update power HAL permissions

### vendor_xiaomi_garnet

- 075775b garnet: Update from OS3.0.301.0.WNRMIXM

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-23

### device_xiaomi_garnet

- c1baf8c garnet: props: Set debug.sf.layer_caching_active_layer_timeout_ms to 1000
- 43a00c1 garnet: power: rework powerhint boosts and camera hints
- f0fbfa9 garnet: sepolicy: Fix Power HAL permissions
- fdef539 Revert "garnet: Drop new powerhint by qcom configs"
- f4ac3c3 garnet: Remove persist.mm.enable.prefetch property
- a5c1364 garnet: power: Add custom Axion power mode hints
- 160dc3f garnet: Add SELinux rules for GNSS and read-ahead
- d41173e garnet: Update Axion flags

### vendor_xiaomi_garnet

- 7c6b976 garnet: Update thermal-normal.conf
- abde6a4 garnet: Drop 32-bit performance libraries

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- dcde5e8 dolby: Fix issues with per device memory and synchronise profile applying with hardware
- 674d53b dolby: Fix unexpected Dolby deactivation when per-device memory is enabled
- 6db29d6 dolby: Update translations from Crowdin
- d9f1dd5 Redesign UI with expressive typography

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-10-10

### device_xiaomi_garnet

- 270868d garnet: "sepolicy: Allow hal_power_default to write to cpu_dma_latency"
- 8782dd3 garnet: Remove APP_START and SYSTEM_UI power hints
- 91d20c2 garnet: Add Axion power mode hints
- b0b3fa8 Revert "garnet: power: Add CPU GPU performance power hints"
- 353ad9c Reapply "garnet: power: Remove CPU GPU performance hints
- ebfcc60 garnet: Load cpq module at boot
- ca474fa garnet: Add camera info init props

### vendor_xiaomi_garnet

- 56c22cb garnet: vendor: Set KGSL default power level
- cdf26c9 garnet: add 32-bit Adreno Gpu libraries
- bd67305 garnet: Update Adreno GPU V@0837.0.9 blobs
- 1f3d1b2 garnet: tune reclaim watermark and swappiness for smoother UX
- ce2ad04 garnet: tune thermal normal profile for better battery life
- 1ecac70 garnet: Rework thermal configuration

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)
