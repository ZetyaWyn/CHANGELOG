
## 2026-09-29
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
