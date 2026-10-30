# Changelog

## 2026-10-30

### device_xiaomi_garnet

- af5fcd4 garnet: parts: add charging bypass toggle Signed-off-by: ZetyaWyn <amruthv780@gmail.com>
- 2ec2ed3 garnet: Bump super size to fix gapps errors
- 0b280a7 garnet: Remove Force triple frame buffers
- 675e7df garnet: Add props to improve battery backup
- f6d054a garnet: Enable SurfaceFlinger's display power timer
- 09d6081 garnet: Update from OS3.0.304.0.WNRMIXM
- 96c5f3f garnet: Update from OS3.0.302.0.WNRMIXM
- 27e6729 garnet: Remove lineage dependencies
- dbe737e sm8250-common: Grant GPU sysfs access for kernel manager and diagnostics
- 69822b2 garnet: init: Read camera sensor for proper about phone camera description
- 4bc6f18 garnet: sepolicy: Update vendor access rules
- da91fc2 garnet: include axion common soc_map
- 10bff44 garnet: Bring up Axion
- 04b8c83 garnet: power: Rework powerhint and add FLING/UI_ANIMATION
- 4e7cab2 garnet: power: Set GPUMinFreq 650MHz & GPUMaxFreq 940MHz on EXPENSIVE_RENDERING
- 8a391f5 garnet: powerhint: Refine performance hints for various scenarios
- 72679be garnet: Change to Arm64 Only
- b3df41c [TMP] garnet: Disable PRODUCT_OTA_ENFORCE_VINTF_KERNEL_REQUIREMENTS
- 2bb9d95 garnet: Enable AOSP surfaceflinger
- 80ccf97 garnet: rootdir: Do not allow foreground tasks to run on CPU7
- 233d3de garnet: rootdir: Move background cpuset to CPU0-1
- a8d5899 garnet: rootdir: Set restricted cpuset to the same CPUs as system-background
- b40f672 garnet: overlay: Remove PowerProfile.POWER_NONE
- c630f23 garnet: disable verbose camera logs
- faf8641 garnet: Set sensors logging level to warn
- 5fa161f garnet: Kill log spam in logcat from SensorService
- 7782eaf garnet: Silence some spammy logging
- 82ac8f6 garnet: Build some missing LDAC libs
- c0eff98 garnet: properties: Enable QCRIL radio power saving
- c6350b4 garnet: props: Disable Logs
- 87a0662 garnet: Disable continuous transaction tracing on all build types
- e2e2b18 garnet: Set display idle time to 0
- dc63699 garnet: enable common build flags
- 0fdec72 garnet: Fix HBM sepolicy issues
- 18a169a garnet: init: Give thermal profiles permissions 05-01 19:34:36.590 W/binder:2826_4(2826): type=1400 audit(0.0:3287): avc:  denied  { write } for  name="sconfig" dev="sysfs" ino=65252 scontext=u:r:system_app:s0 tcontext=u:object_r:sysfs_thermal:s0 tclass=file permissive=0 05-01 19:34:36.594 W/FileUtils(2826): No such file /sys/class/thermal/thermal_message/sconfig for writing 05-01 19:34:36.594 W/FileUtils(2826): java.io.FileNotFoundException: /sys/class/thermal/thermal_message/sconfig: open failed: EACCES (Permission denied)
- 493666b garnet: Fix gamebar GPU info
- 4f702a0 garnet: Drop bypass charging and update translations
- 20acb0a garnet: parts: Enable predictive back gestures
- b2d61e8 garnet: parts: Refine UI
- e9e01f0 garnet: parts: Move GameBar strings to resources and translate
- 79abc6d garnet: parts: Apply expressive design style
- 5e182a9 garnet: parts: Add translations for pt-BR, pt-PT, hi, fr, de, it, ar, ja, ko, az, ca, ckb, el, en-rAU, en-rCA, en-rGB, en-rIN, fa, ga-rIE, hu, iw, nn-rNO, pl, ro, sl, sq, ta, ug and vi
- 523224d garnet: parts: Import from xiaomi_sdm845-common https://github.com/LineageOS/android_device_xiaomi_sdm845-common/tree/e261035d91b34cf0fdf0f012927e06a2bcdb03ed/parts
- bd20b1a garnet: Speed profile services and wifi-service to reduce RAM and storage
- b7eaa77 garnet: init: rm package cache on early boot
- d937ac2 garnet: fstab: set readahead_size_kb=128 to data
- a6ad33c garnet: rootdir: Set correct permission for ntsync
- e960a7a garnet: Load ntsync module at boot
- 6d4eb27 garnet: Add SM7435 init script
- 163a132 garnet: fix off-mode charging trigger
- 10ff61b garnet: Add missing permission for charging
- eac9cef garnet: Drop permissive mode and label charging policy
- 87838d0 garnet: Implement thermal-based charging control
- 9219bb9 garnet: Guard erofs hints for erofs build
- ffa2b85 garnet: Add erofs compress hints
- e0152e9 garnet: Build gapps by default
- 03ad95d garnet: Switch system partitions to EROFS
- 39e1f8f garnet: rootdir: Use foreground cpuset/uclamp for gralloc Makes sure rendering has enough capacity.
- 2744f9e garnet: rootdir: Use foreground uclamp for hwcomposer Matches SF, makes sure rendering always has enough capacity.
- 2045b99 garnet: debloat: Remove Pixel Live Wallpaper
- 95332fc garnet: debloat: Drop jelly app
- 25591b3 garnet: Include app debloater
- a8e8374 garnet: Switch to 8GB Dalvik heap config
- 114e1bd garnet: overlay: Set default pin amount for home app
- 51cd8a0 garnet: overlay: Add webview pinning
- dda38f3 garnet: Remove duplicate heap growth limit
- 1c1a3b9 garnet: sepolicy: Neverallow app open access to /dev/ashmem
- 6673a80 garnet: Add unix to hide Magisk in banking apps
- f7915ae garnet: init: Give proper permissions for /dev/diag
- f72eebc garnet: Disable QCOM system daemon
- 33ff70e garnet: rootdir: Remove IO read_ahead_kb tune
- 9e1b222 garnet: audio: Route spatial output to Bluetooth
- 7c6d27a garnet: rootdir: Set swappiness to 60
- 8dd0ccd garnet: rootdir: Don't configure zram in QCOM's init post boot script
- 905db5c garnet: camera: Set torch default strength level to max
- ed77494 garnet: Implement torch light control
- c9dcc2a garnet: Fixing connecting BLE (bt 5.x) devices (smart watches, etc.)
- 68b2fa3 garnet: audio: Add fallback SW A2DP routes
- 74adb7d garnet: Audio: Enable support of HW Accelerated Effects
- 8e17084 garnet: audio: Add hardware accelerated audio effect
- 35016c3 garnet: audio: Add DSEE effect
- 092c3d9 garnet: audio: Fix overly loud notification sound
- 1861307 garnet: Move c2_manifest_vendor.xml to device tree
- 3ed2a34 garnet: Import QCOM audio effects from OnePlus 9R
- 63b139d garnet: audio: use QCOM Implementation for Audio Effects
- 200de6c garnet: Include Sony Dolby Atmos and Sync with Spatial Audio
- c22306d garnet: props: Increase audio offload buffer size from 32KB to 64KB
- ffedceb garnet: audio: Fix mic issues in apps like WhatsApp
- 946b34f garnet: DeviceAsWebcam: set HQ mode as default
- f1a89a4 garnet: DeviceAsWebcam: disable USAGE_VIDEO_ENCODE ImageReader flag
- 6507ab8 garnet: Build DeviceAsWebcam service
- e47be11 garnet: Setup DeviceAsWebcam
- d2e1d8e garnet: Limit background CPU utilization
- ea2dbd4 garnet: Limit dex2oat cpu utilization
- 96eb8cc garnet: overlay: Enable PowerOffAlarmService
- e86d4eb garnet: sepolicy: Allow PowerOffAlarm app to find alarm service
- 66436bd garnet: rootdir: fix battery drain due to statsd
- aab7a91 garnet: overlay: Improve auto brightness
- 11a4948 garnet: Tweak some auto brightness configs
- c1f7d13 garnet: Optimize auto brightness adjustment
- 2a50d97 garnet: overlay: lower autoBrightness Debounce
- ccbe64d garnet: overlay: Increase auto brightness debounce
- 87e1898 garnet: overlay: Add overlay to improve signal reception
- 5f35312 garnet: overlay: Enable Smart 5G
- 559d14d garnet: overlay: Define OEM fast charge sysfs node
- dd22020 garnet: overlay: Enable Smart Pixels
- 6093150 garnet: overlay: Disable high performance transitions
- 0d2d4ca garnet: Decouple interactive state from display
- 77bdf05 garnet: Add SystemUI restart in restart advanced menu
- 55486ce garnet: Enable LTO Optimizations
- db43d33 garnet: Overlay: Define config_screenRecorderAVCProfileLevel
- 030cea3 garnet: wifi: Enable Optimized Power Management
- a8ec194 garnet: wifi: Disable TDLS offchannel
- 75db85f garnet: wifi: Smarter decisions on whether to use a 2 or 5Ghz AP
- da31d41 garnet: props: More VoNR props
- c07bcd7 garnet: Enable VoNR Calls support Change-Id: I3cc986fd2352dc266e0d423767192c15c3669c5b Signed-off-by: Omar Mohamed <omarcoptan9@gmail.com> Signed-off-by: Z E U S <iamdrzeus14@gmail.com>
- 80a444c garnet: Import carrier configuration from peridot
- 1b7e1e3 sm8250-common: overlay: Enable VoNR on Jio 5G
- a40b155 garnet: overlay: Set 5G threshold bandwidth to 0
- 9070825 sm8250-common: overlay: Only allow 5G SA on Jio
- a64b3cf garnet: overlay: Set LTE+ threshold bandwidth to 0
- 1108eee garnet: overlay: Globally enable LTE+ icon
- 45ad428 garnet: overlay: Allow VoLTE and VoWiFi by default
- bdb4942 garnet: remove FRP lock
- 1fe13d0 garnet: tune HWUI and SurfaceFlinger performance
- 1a4e56a garnet: Enable frame pacing for smoother visual performance
- 81bb9e2 garnet: properties: Set persist.sys.purgeable_assets=1
- a1ed146 garnet: Enable debug.performance.tuning
- a5b4244 garnet: Apply dex2oat optimizations
- 24b3aa1 garnet: disable_gl_backpressure
- 880d7c1 garnet: Set ro.netflix.bsp_rev
- aef40d5 garnet: Disable EGL image tracking
- 0dd1d7a garnet: sepolicy: Label bluetooth props
- 1534ea6 garnet: Enable TWS plus feature using persist property
- 27bf59e garnet: Enable Qualcomm TrueWireless™ Stereo
- 48585b5 garnet: sepolicy: Allow fingerprint HAL to access performance and sensor nodes
- c494242 garnet: Allow qti init shell to open/write page cluster size
- d20ac2b garnet: sepolicy: Allow system_app to access zram sysfs nodes
- 33ba12b garnet: sepolicy: Dontaudit camera hal default_prop
- 392ca58 garnet: properties: camera: enable aux camera access for all apps
- 9b0a3ac garnet: sepolicy: Address system suspend denials
- 4109c24 garnet: sepolicy: Allow init/vold to write storage sysfs parameters
- caecd45 garnet: sepolicy: Label UFS discard_max_bytes
- 57831b6 garnet: Set BOOT_SECURITY_PATCH
- 95a075d garnet: Set VENDOR_SECURITY_PATCH To PLATFORM
- a1b1cfc garnet: disable FW roaming when in idle mode When device is idle, disable FW roaming (LOW RSSI roam, high band roam) to save power
- 058dcfc garnet: overlay: Set Wi-Fi 6 support
- d04be26 garnet: Add com.android.bluetooth context to seapp_contexts
- 9e18b94 garnet: SEPolicy: Grant system_app access to thermal sysfs files

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

- 90fba89 garnet: Update from OS3.0.304.0.WNRMIXM

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
