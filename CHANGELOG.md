
## 2026-09-29
## 2026-10-23

### device_xiaomi_garnet

- 369d7d3 garnet: parts: Enable predictive back gestures
- 94c1cf7 garnet: parts: Refine UI
- af46a81 garnet: parts: Move GameBar strings to resources and translate
- a7ba289 garnet: parts: Apply expressive design style
- bfaa348 garnet: parts: Add translations for pt-BR, pt-PT, hi, fr, de, it, ar, ja, ko, az, ca, ckb, el, en-rAU, en-rCA, en-rGB, en-rIN, fa, ga-rIE, hu, iw, nn-rNO, pl, ro, sl, sq, ta, ug and vi
- 49119c2 garnet: sepolicy: Allow init/vold to write storage sysfs parameters
- 4ad39ee garnet: sepolicy: Allow system_app to access zram sysfs nodes
- 61588ba garnet: sepolicy: Dontaudit camera hal default_prop
- 5297264 garnet: sepolicy: Fix Power HAL permissions
- fdef539 Revert "garnet: Drop new powerhint by qcom configs"
- d5b06e8 garnet: sepolicy: Label bluetooth props
- 4ed9f70 garnet: sepolicy: Allow fingerprint HAL to access performance and sensor nodes
- 5950b18 garnet: Allow qti init shell to open/write page cluster size
- 1049e57 garnet: Fixing connecting BLE (bt 5.x) devices (smart watches, etc.)
- aafaea9 garnet: Add SM7435 init script
- 7199b30 garnet: overlay: Improve status bar visual consistency
- ab5d821 garnet: include axion common soc_map
- e9929a6 garnet: audio: Add fallback SW A2DP routes
- f4ac3c3 garnet: Remove persist.mm.enable.prefetch property
- b6c03fd garnet: Disable QCOM system daemon
- 7573f1d garnet: sepolicy: Grant system_app access to hal_mlipay_hwservice
- 0a75e22 [TMP] garnet: Disable PRODUCT_OTA_ENFORCE_VINTF_KERNEL_REQUIREMENTS
- a5c1364 garnet: power: Add custom Axion power mode hints
- dbc0236 garnet: sepolicy: Allow system_server to write to audioserver_tmpfs
- 4163359 garnet: sepolicy: Add sys_nice capability to hal_fingerprint_default
- f72c94e garnet: sepolicy: Label missing sysfs_wakeup nodes
- 7b1cf71 garnet: sepolicy: Allow system_suspend to read sysfs_wakeup files
- 160dc3f garnet: Add SELinux rules for GNSS and read-ahead
- a57ff0d sm8250-common: Grant GPU sysfs access for kernel manager and diagnostics
- c743b4d garnet: rootdir: Remove IO read_ahead_kb tune
- 14f0471 garnet: init: Read camera sensor for proper about phone camera description
- 6340f74 garnet: Wire up per fps sf durations
- 051bc92 garnet: Set base sf work durations duration props from stock
- 6231c3b Revert "garnet: Update sf duration to 12.3ms"
- 7a5b080 garnet: rootdir: Set swappiness to 60
- a663b04 garnet: init: Give proper permissions for /dev/diag
- d41173e garnet: Update Axion flags
- 18e96ac garnet: audio: Add hardware accelerated audio effect
- 36a1503 garnet: Change to Arm64 Only
- 0352f4b garnet: camera: Set torch default strength level to max

### vendor_xiaomi_garnet

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
- 8c0b475 garnet: Disable QCOM system daemon
- 8782dd3 garnet: Remove APP_START and SYSTEM_UI power hints
- 0ea7929 garnet: sepolicy: Grant system_app access to hal_mlipay_hwservice
- 7b52176 garnet: Add com.android.bluetooth context to seapp_contexts
- 376640d [TMP] garnet: Disable PRODUCT_OTA_ENFORCE_VINTF_KERNEL_REQUIREMENTS
- 91d20c2 garnet: Add Axion power mode hints
- 48593f9 garnet: sepolicy: Allow system_server to write to audioserver_tmpfs
- 268ff12 garnet: sepolicy: Add sys_nice capability to hal_fingerprint_default
- 0f59c87 garnet: sepolicy: Label missing sysfs_wakeup nodes
- 2c7c2e6 garnet: sepolicy: Allow system_suspend to read sysfs_wakeup files
- f9e428a garnet: power: Set GPUMinFreq 650MHz & GPUMaxFreq 940MHz on EXPENSIVE_RENDERING
- 7e4d2be garnet: powerhint: Refine performance hints for various scenarios
- b6c64d3 Revert "garnet: Drop new powerhint by qcom configs"
- b0b3fa8 Revert "garnet: power: Add CPU GPU performance power hints"
- 353ad9c Reapply "garnet: power: Remove CPU GPU performance hints
- 8eb301b garnet: Add SELinux rules for GNSS and read-ahead

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

### device_xiaomi_garnet

- ebfcc60 garnet: Load cpq module at boot
- 49e89c3 garnet: rootdir: Set swappiness to 60
- ca474fa garnet: Add camera info init props
- be0f774 garnet: Grant GPU sysfs access for kernel manager and diagnostics
- 6483174 garnet: include axion common soc_map
- d125518 garnet: rootdir: Remove IO read_ahead_kb tune
- 51a42de garnet: init: Give proper permissions for /dev/diag
- 23766b4 garnet: Update Axion flags

### vendor_xiaomi_garnet

- 231d607 garnet: Drop 32-bit performance libraries
- 1c79a1d garnet: Drop 32 Libs
- 5452447 garnet: Restore eUICC mirilhook from 35d1c0f
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
