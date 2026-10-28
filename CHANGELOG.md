# Changelog

## 2026-10-28

### device_xiaomi_garnet

- 948d974 garnet: Update from OS3.0.304.0.WNRMIXM
- 25d3f83 garnet: Update from OS3.0.302.0.WNRMIXM
- c0c6edc garnet: Remove lineage dependencies
- a5a3093 sm8250-common: Grant GPU sysfs access for kernel manager and diagnostics
- dcae583 garnet: init: Read camera sensor for proper about phone camera description
- f826f28 garnet: sepolicy: Update vendor access rules
- 0f58270 garnet: include axion common soc_map
- efbc490 garnet: Bring up Axion
- 1714438 garnet: power: Rework powerhint and add FLING/UI_ANIMATION
- 7425071 garnet: power: Set GPUMinFreq 650MHz & GPUMaxFreq 940MHz on EXPENSIVE_RENDERING
- 1952263 garnet: powerhint: Refine performance hints for various scenarios
- c244941 garnet: Change to Arm64 Only
- b44c7a1 [TMP] garnet: Disable PRODUCT_OTA_ENFORCE_VINTF_KERNEL_REQUIREMENTS
- 3c64f9b garnet: Enable AOSP surfaceflinger
- c9fa1c2 garnet: rootdir: Do not allow foreground tasks to run on CPU7
- ac29a37 garnet: rootdir: Move background cpuset to CPU0-1
- edeb99e garnet: rootdir: Set restricted cpuset to the same CPUs as system-background
- 105621f garnet: overlay: Remove PowerProfile.POWER_NONE
- a80bdcd garnet: disable verbose camera logs
- 4d661a2 garnet: Set sensors logging level to warn
- 131280e garnet: Kill log spam in logcat from SensorService
- ff7bf29 garnet: Silence some spammy logging
- 5ae81be garnet: Build some missing LDAC libs
- 7131211 garnet: properties: Enable QCRIL radio power saving
- 0c18cf3 garnet: props: Disable Logs
- dc577f5 garnet: Disable continuous transaction tracing on all build types
- 7f54650 garnet: Set display idle time to 0
- 45f5698 garnet: enable common build flags
- dd6e7b9 garnet: Fix HBM sepolicy issues
- e8cb08c garnet: init: Give thermal profiles permissions 05-01 19:34:36.590 W/binder:2826_4(2826): type=1400 audit(0.0:3287): avc:  denied  { write } for  name="sconfig" dev="sysfs" ino=65252 scontext=u:r:system_app:s0 tcontext=u:object_r:sysfs_thermal:s0 tclass=file permissive=0 05-01 19:34:36.594 W/FileUtils(2826): No such file /sys/class/thermal/thermal_message/sconfig for writing 05-01 19:34:36.594 W/FileUtils(2826): java.io.FileNotFoundException: /sys/class/thermal/thermal_message/sconfig: open failed: EACCES (Permission denied)
- cd96c6e garnet: Fix gamebar GPU info
- 51ea3bc garnet: Drop bypass charging and update translations
- 4fdbb40 garnet: parts: Enable predictive back gestures
- 8feaa0c garnet: parts: Refine UI
- 3ff3439 garnet: parts: Move GameBar strings to resources and translate
- f891c2d garnet: parts: Apply expressive design style
- c89b09b garnet: parts: Add translations for pt-BR, pt-PT, hi, fr, de, it, ar, ja, ko, az, ca, ckb, el, en-rAU, en-rCA, en-rGB, en-rIN, fa, ga-rIE, hu, iw, nn-rNO, pl, ro, sl, sq, ta, ug and vi
- 02aabf9 garnet: parts: Import from xiaomi_sdm845-common https://github.com/LineageOS/android_device_xiaomi_sdm845-common/tree/e261035d91b34cf0fdf0f012927e06a2bcdb03ed/parts
- b34e046 garnet: Speed profile services and wifi-service to reduce RAM and storage
- a7c8379 garnet: init: rm package cache on early boot
- 1118103 garnet: fstab: set readahead_size_kb=128 to data
- 0ada345 garnet: rootdir: Set correct permission for ntsync
- 7d5355d garnet: Load ntsync module at boot
- a4e1c04 garnet: Add SM7435 init script
- 893ba3b garnet: fix off-mode charging trigger
- 773171b garnet: Add missing permission for charging
- 12b96b5 garnet: Drop permissive mode and label charging policy
- 6372c96 garnet: Implement thermal-based charging control
- 9f1640e garnet: Guard erofs hints for erofs build
- f1dde91 garnet: Add erofs compress hints
- 1144131 garnet: Build gapps by default
- a4e4ca9 garnet: Switch system partitions to EROFS
- 91d74bf garnet: rootdir: Use foreground cpuset/uclamp for gralloc Makes sure rendering has enough capacity.
- b6ff2d8 garnet: rootdir: Use foreground uclamp for hwcomposer Matches SF, makes sure rendering always has enough capacity.
- f7f6bfa garnet: debloat: Remove Pixel Live Wallpaper
- 644013b garnet: debloat: Drop jelly app
- 0f425e0 garnet: Include app debloater
- d2e99df garnet: Switch to 8GB Dalvik heap config
- 064ec22 garnet: overlay: Set default pin amount for home app
- 291ec07 garnet: overlay: Add webview pinning
- 64dc53e garnet: Remove duplicate heap growth limit
- c6e298a garnet: sepolicy: Neverallow app open access to /dev/ashmem
- 55378ed garnet: Add unix to hide Magisk in banking apps
- 1349242 garnet: init: Give proper permissions for /dev/diag
- 819c374 garnet: Disable QCOM system daemon
- 92ce168 garnet: rootdir: Remove IO read_ahead_kb tune
- fb87f0d garnet: audio: Route spatial output to Bluetooth
- 6c192bd garnet: rootdir: Set swappiness to 60
- 36911fa garnet: rootdir: Don't configure zram in QCOM's init post boot script
- 39f073a garnet: camera: Set torch default strength level to max
- e9d4dbe garnet: Implement torch light control
- 564c7fd garnet: Fixing connecting BLE (bt 5.x) devices (smart watches, etc.)
- c842e28 garnet: audio: Add fallback SW A2DP routes
- 0944d4a garnet: Audio: Enable support of HW Accelerated Effects
- e689390 garnet: audio: Add hardware accelerated audio effect
- 548fb22 garnet: audio: Add DSEE effect
- 458357e garnet: audio: Fix overly loud notification sound
- d3c1480 garnet: Move c2_manifest_vendor.xml to device tree
- 3c4b9c2 garnet: Import QCOM audio effects from OnePlus 9R
- 20ad150 garnet: audio: use QCOM Implementation for Audio Effects
- 6edf796 garnet: Include Sony Dolby Atmos and Sync with Spatial Audio
- 60faa54 garnet: props: Increase audio offload buffer size from 32KB to 64KB
- 476975d garnet: audio: Fix mic issues in apps like WhatsApp
- ad7bcec garnet: DeviceAsWebcam: set HQ mode as default
- 4de8ee0 garnet: DeviceAsWebcam: disable USAGE_VIDEO_ENCODE ImageReader flag
- c50df47 garnet: Build DeviceAsWebcam service
- 00133e8 garnet: Setup DeviceAsWebcam
- d496460 garnet: Limit background CPU utilization
- f0f2304 garnet: Limit dex2oat cpu utilization
- b944115 garnet: overlay: Enable PowerOffAlarmService
- 083f868 garnet: sepolicy: Allow PowerOffAlarm app to find alarm service
- fb2e9ff garnet: rootdir: fix battery drain due to statsd
- 3f1e3bc garnet: overlay: Improve auto brightness
- 9ec23b3 garnet: Tweak some auto brightness configs
- 866c9cc garnet: Optimize auto brightness adjustment
- 5d788e6 garnet: overlay: lower autoBrightness Debounce
- ef97dc9 garnet: overlay: Increase auto brightness debounce
- 850143c garnet: overlay: Add overlay to improve signal reception
- 5888166 garnet: overlay: Enable Smart 5G
- d99f7a0 garnet: overlay: Define OEM fast charge sysfs node
- 294d9a2 garnet: overlay: Enable Smart Pixels
- 37f1980 garnet: overlay: Disable high performance transitions
- 08c492d garnet: Decouple interactive state from display
- 267e240 garnet: Add SystemUI restart in restart advanced menu
- 6268ad3 garnet: Enable LTO Optimizations
- 5c38f1d garnet: Overlay: Define config_screenRecorderAVCProfileLevel
- 7e19226 garnet: wifi: Enable Optimized Power Management
- a05b118 garnet: wifi: Disable TDLS offchannel
- 060a962 garnet: wifi: Smarter decisions on whether to use a 2 or 5Ghz AP
- d142768 garnet: props: More VoNR props
- 9779726 garnet: Enable VoNR Calls support Change-Id: I3cc986fd2352dc266e0d423767192c15c3669c5b Signed-off-by: Omar Mohamed <omarcoptan9@gmail.com> Signed-off-by: Z E U S <iamdrzeus14@gmail.com>
- 6083bfb garnet: Import carrier configuration from peridot
- bb2dff9 sm8250-common: overlay: Enable VoNR on Jio 5G
- c46cb93 garnet: overlay: Set 5G threshold bandwidth to 0
- bd9c962 sm8250-common: overlay: Only allow 5G SA on Jio
- c087978 garnet: overlay: Set LTE+ threshold bandwidth to 0
- 177192a garnet: overlay: Globally enable LTE+ icon
- 17e89d3 garnet: overlay: Allow VoLTE and VoWiFi by default
- 82422d1 garnet: remove FRP lock
- 1a5a26b garnet: tune HWUI and SurfaceFlinger performance
- 13384ca garnet: Enable frame pacing for smoother visual performance
- 080dbe2 garnet: properties: Set persist.sys.purgeable_assets=1
- a00bb70 garnet: Enable debug.performance.tuning
- b4ce4f2 garnet: Apply dex2oat optimizations
- f0814a2 garnet: disable_gl_backpressure
- 6642eb9 garnet: Set ro.netflix.bsp_rev
- 9b2f175 garnet: Disable EGL image tracking
- 98090db garnet: sepolicy: Label bluetooth props
- bcf5d3f garnet: Enable TWS plus feature using persist property
- c8a9140 garnet: Enable Qualcomm TrueWireless™ Stereo
- ee176d6 garnet: sepolicy: Allow fingerprint HAL to access performance and sensor nodes
- 9ef12c3 garnet: Allow qti init shell to open/write page cluster size
- df80ebc garnet: sepolicy: Allow system_app to access zram sysfs nodes
- 9435ea3 garnet: sepolicy: Dontaudit camera hal default_prop
- e28767f garnet: properties: camera: enable aux camera access for all apps
- 1f2e328 garnet: sepolicy: Address system suspend denials
- ee49a2b garnet: sepolicy: Allow init/vold to write storage sysfs parameters
- ecffa7b garnet: sepolicy: Label UFS discard_max_bytes
- 0483269 garnet: Set BOOT_SECURITY_PATCH
- 60273ec garnet: Set VENDOR_SECURITY_PATCH To PLATFORM
- 96775f5 garnet: disable FW roaming when in idle mode When device is idle, disable FW roaming (LOW RSSI roam, high band roam) to save power
- 9d07c4b garnet: overlay: Set Wi-Fi 6 support
- 99c4e1f garnet: Add com.android.bluetooth context to seapp_contexts
- 7388785 garnet: SEPolicy: Grant system_app access to thermal sysfs files
- ba5b4b8 garnet: Drop qesdk blobs
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

- No new commits.

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
- 36bccd7 garnet: Add props to improve battery backup

### vendor_xiaomi_garnet

- 5de2d90 garnet: Update from OS3.0.302.0.WNRMIXM
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
- 0e72218 garnet: Drop 32 Libs
- f84f439 garnet: Restore eUICC mirilhook from 35d1c0f

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- dcde5e8 dolby: Fix issues with per device memory and synchronise profile applying with hardware
- 674d53b dolby: Fix unexpected Dolby deactivation when per-device memory is enabled
- 6db29d6 dolby: Update translations from Crowdin
- d9f1dd5 Redesign UI with expressive typography
- 754bb43 dolby: Fix master toggle reactivation and synchronize QS tile state

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
- be0f774 garnet: Grant GPU sysfs access for kernel manager and diagnostics

### vendor_xiaomi_garnet

- 56c22cb garnet: vendor: Set KGSL default power level
- 951c8e1 garnet: init: Reset readahead values for 128 always
- 47b12df garnet: Don't configure zram in post boot scripts
- fafd217 garnet: switch to deep suspend-to-RAM
- 2c21f42 garnet: Add missing Leica video filter
- cdf26c9 garnet: add 32-bit Adreno Gpu libraries
- bd67305 garnet: Update Adreno GPU V@0837.0.9 blobs
- 1f3d1b2 garnet: tune reclaim watermark and swappiness for smoother UX
- 0636b2f garnet: switch default I/O scheduler to mq-deadline
- 1a7d5de garnet: Import QCOM audio effects from OnePlus 9R
- ce2ad04 garnet: tune thermal normal profile for better battery life
- 1ecac70 garnet: Rework thermal configuration
- 2cd4c6b garnet: expand WALT game list and enable lib mask force
- f3358c6 garnet: update shared_libs for greatwhite driver
- 34b286a garnet: update GPU driver blobs from greatwhite V@0863.1
- ccecf22 garnet: Remove again QDESK and Qquard

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
