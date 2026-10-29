# Changelog

## 2026-10-29

### device_xiaomi_garnet

- 51c9ab2 garnet: Enable SurfaceFlinger's display power timer
- d342874 garnet: Update from OS3.0.304.0.WNRMIXM
- 48dfecb garnet: Update from OS3.0.302.0.WNRMIXM
- e8481d0 garnet: Remove lineage dependencies
- 828e7da sm8250-common: Grant GPU sysfs access for kernel manager and diagnostics
- 86a5fcb garnet: init: Read camera sensor for proper about phone camera description
- cd1063f garnet: sepolicy: Update vendor access rules
- a4a982d garnet: include axion common soc_map
- 86ceafa garnet: Bring up Axion
- cffe17b garnet: power: Rework powerhint and add FLING/UI_ANIMATION
- 16f0d98 garnet: power: Set GPUMinFreq 650MHz & GPUMaxFreq 940MHz on EXPENSIVE_RENDERING
- 58fe330 garnet: powerhint: Refine performance hints for various scenarios
- 0123897 garnet: Change to Arm64 Only
- 078448c [TMP] garnet: Disable PRODUCT_OTA_ENFORCE_VINTF_KERNEL_REQUIREMENTS
- 2e58ec1 garnet: Enable AOSP surfaceflinger
- c347b1f garnet: rootdir: Do not allow foreground tasks to run on CPU7
- 9331fe9 garnet: rootdir: Move background cpuset to CPU0-1
- 9342d11 garnet: rootdir: Set restricted cpuset to the same CPUs as system-background
- 92cb25f garnet: overlay: Remove PowerProfile.POWER_NONE
- 3028442 garnet: disable verbose camera logs
- d093e6b garnet: Set sensors logging level to warn
- 2998b69 garnet: Kill log spam in logcat from SensorService
- 4ab30ff garnet: Silence some spammy logging
- d2df206 garnet: Build some missing LDAC libs
- 313a155 garnet: properties: Enable QCRIL radio power saving
- b35fe82 garnet: props: Disable Logs
- ff93014 garnet: Disable continuous transaction tracing on all build types
- 2baf93b garnet: Set display idle time to 0
- 21a28f7 garnet: enable common build flags
- 6474572 garnet: Fix HBM sepolicy issues
- 005ae4a garnet: init: Give thermal profiles permissions 05-01 19:34:36.590 W/binder:2826_4(2826): type=1400 audit(0.0:3287): avc:  denied  { write } for  name="sconfig" dev="sysfs" ino=65252 scontext=u:r:system_app:s0 tcontext=u:object_r:sysfs_thermal:s0 tclass=file permissive=0 05-01 19:34:36.594 W/FileUtils(2826): No such file /sys/class/thermal/thermal_message/sconfig for writing 05-01 19:34:36.594 W/FileUtils(2826): java.io.FileNotFoundException: /sys/class/thermal/thermal_message/sconfig: open failed: EACCES (Permission denied)
- 4d0d910 garnet: Fix gamebar GPU info
- 3864cb7 garnet: Drop bypass charging and update translations
- 415b7da garnet: parts: Enable predictive back gestures
- 4ebd993 garnet: parts: Refine UI
- 9a20ec5 garnet: parts: Move GameBar strings to resources and translate
- 7598d4e garnet: parts: Apply expressive design style
- aac8fcb garnet: parts: Add translations for pt-BR, pt-PT, hi, fr, de, it, ar, ja, ko, az, ca, ckb, el, en-rAU, en-rCA, en-rGB, en-rIN, fa, ga-rIE, hu, iw, nn-rNO, pl, ro, sl, sq, ta, ug and vi
- 6e2a0bb garnet: parts: Import from xiaomi_sdm845-common https://github.com/LineageOS/android_device_xiaomi_sdm845-common/tree/e261035d91b34cf0fdf0f012927e06a2bcdb03ed/parts
- fb3c761 garnet: Speed profile services and wifi-service to reduce RAM and storage
- ab6852f garnet: init: rm package cache on early boot
- 3bd91b1 garnet: fstab: set readahead_size_kb=128 to data
- 3400b8d garnet: rootdir: Set correct permission for ntsync
- 468246d garnet: Load ntsync module at boot
- cb3ffbd garnet: Add SM7435 init script
- cf6f2a4 garnet: fix off-mode charging trigger
- 413c05f garnet: Add missing permission for charging
- ddecb0d garnet: Drop permissive mode and label charging policy
- 69b9243 garnet: Implement thermal-based charging control
- 59837e2 garnet: Guard erofs hints for erofs build
- d0594c0 garnet: Add erofs compress hints
- 8230089 garnet: Build gapps by default
- 57a7429 garnet: Switch system partitions to EROFS
- 66e4b1d garnet: rootdir: Use foreground cpuset/uclamp for gralloc Makes sure rendering has enough capacity.
- 9b83687 garnet: rootdir: Use foreground uclamp for hwcomposer Matches SF, makes sure rendering always has enough capacity.
- c710663 garnet: debloat: Remove Pixel Live Wallpaper
- a8a366f garnet: debloat: Drop jelly app
- be7ba2d garnet: Include app debloater
- 4073715 garnet: Switch to 8GB Dalvik heap config
- c82e2c8 garnet: overlay: Set default pin amount for home app
- 6a2adca garnet: overlay: Add webview pinning
- 1b6499b garnet: Remove duplicate heap growth limit
- 36458a7 garnet: sepolicy: Neverallow app open access to /dev/ashmem
- b6ea189 garnet: Add unix to hide Magisk in banking apps
- ea3d932 garnet: init: Give proper permissions for /dev/diag
- 9975bb2 garnet: Disable QCOM system daemon
- e01f507 garnet: rootdir: Remove IO read_ahead_kb tune
- 72bbfdb garnet: audio: Route spatial output to Bluetooth
- d22a6f1 garnet: rootdir: Set swappiness to 60
- 810021c garnet: rootdir: Don't configure zram in QCOM's init post boot script
- f5a49d2 garnet: camera: Set torch default strength level to max
- e838c4e garnet: Implement torch light control
- d7821a5 garnet: Fixing connecting BLE (bt 5.x) devices (smart watches, etc.)
- 50c22cd garnet: audio: Add fallback SW A2DP routes
- 3af418e garnet: Audio: Enable support of HW Accelerated Effects
- c2c90fd garnet: audio: Add hardware accelerated audio effect
- b244d89 garnet: audio: Add DSEE effect
- ce38e67 garnet: audio: Fix overly loud notification sound
- c3d71d7 garnet: Move c2_manifest_vendor.xml to device tree
- 61d1fb2 garnet: Import QCOM audio effects from OnePlus 9R
- 78fee08 garnet: audio: use QCOM Implementation for Audio Effects
- 10c106c garnet: Include Sony Dolby Atmos and Sync with Spatial Audio
- 52f3e43 garnet: props: Increase audio offload buffer size from 32KB to 64KB
- b34b76f garnet: audio: Fix mic issues in apps like WhatsApp
- 8a44d65 garnet: DeviceAsWebcam: set HQ mode as default
- 1cb8a2b garnet: DeviceAsWebcam: disable USAGE_VIDEO_ENCODE ImageReader flag
- 022086c garnet: Build DeviceAsWebcam service
- 9886862 garnet: Setup DeviceAsWebcam
- 83f31a5 garnet: Limit background CPU utilization
- a5260e8 garnet: Limit dex2oat cpu utilization
- 3eda3b7 garnet: overlay: Enable PowerOffAlarmService
- 0725fa0 garnet: sepolicy: Allow PowerOffAlarm app to find alarm service
- 293c992 garnet: rootdir: fix battery drain due to statsd
- 5bc7fa9 garnet: overlay: Improve auto brightness
- 1018b0f garnet: Tweak some auto brightness configs
- fbb1990 garnet: Optimize auto brightness adjustment
- 742674f garnet: overlay: lower autoBrightness Debounce
- 6665719 garnet: overlay: Increase auto brightness debounce
- 084487b garnet: overlay: Add overlay to improve signal reception
- bad3a43 garnet: overlay: Enable Smart 5G
- ce4f4f4 garnet: overlay: Define OEM fast charge sysfs node
- b6ec1ff garnet: overlay: Enable Smart Pixels
- de09250 garnet: overlay: Disable high performance transitions
- aafa435 garnet: Decouple interactive state from display
- 2e49dfe garnet: Add SystemUI restart in restart advanced menu
- 1f5c0ae garnet: Enable LTO Optimizations
- 1eddab9 garnet: Overlay: Define config_screenRecorderAVCProfileLevel
- 3f3561d garnet: wifi: Enable Optimized Power Management
- 96246dc garnet: wifi: Disable TDLS offchannel
- 6e73a4e garnet: wifi: Smarter decisions on whether to use a 2 or 5Ghz AP
- c8d48aa garnet: props: More VoNR props
- 8a02667 garnet: Enable VoNR Calls support Change-Id: I3cc986fd2352dc266e0d423767192c15c3669c5b Signed-off-by: Omar Mohamed <omarcoptan9@gmail.com> Signed-off-by: Z E U S <iamdrzeus14@gmail.com>
- 466b13b garnet: Import carrier configuration from peridot
- c6b8047 sm8250-common: overlay: Enable VoNR on Jio 5G
- f8e0270 garnet: overlay: Set 5G threshold bandwidth to 0
- 7bed758 sm8250-common: overlay: Only allow 5G SA on Jio
- 071f851 garnet: overlay: Set LTE+ threshold bandwidth to 0
- 7e3cbf0 garnet: overlay: Globally enable LTE+ icon
- b68c913 garnet: overlay: Allow VoLTE and VoWiFi by default
- b8b646c garnet: remove FRP lock
- 9760435 garnet: tune HWUI and SurfaceFlinger performance
- 0193375 garnet: Enable frame pacing for smoother visual performance
- 1239bb0 garnet: properties: Set persist.sys.purgeable_assets=1
- 1103c9a garnet: Enable debug.performance.tuning
- 5e5c4db garnet: Apply dex2oat optimizations
- 740c457 garnet: disable_gl_backpressure
- a79b455 garnet: Set ro.netflix.bsp_rev
- 47cf2a9 garnet: Disable EGL image tracking
- 3179d84 garnet: sepolicy: Label bluetooth props
- 039d806 garnet: Enable TWS plus feature using persist property
- ae6d5b1 garnet: Enable Qualcomm TrueWireless™ Stereo
- 3274a4c garnet: sepolicy: Allow fingerprint HAL to access performance and sensor nodes
- c8203c1 garnet: Allow qti init shell to open/write page cluster size
- 78b7d2e garnet: sepolicy: Allow system_app to access zram sysfs nodes
- 9e27b62 garnet: sepolicy: Dontaudit camera hal default_prop
- 6d25083 garnet: properties: camera: enable aux camera access for all apps
- 7088616 garnet: sepolicy: Address system suspend denials

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
