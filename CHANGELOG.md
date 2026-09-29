## 2026-09-08

## 2026-09-29

### device_xiaomi_garnet

- c85b9a4 garnet: Add camera info init props
- 44b672c garnet: Grant GPU sysfs access for kernel manager and diagnostics
- b40a723 garnet: include axion common soc_map
- b25475b garnet: rootdir: Remove IO read_ahead_kb tune
- e990922 garnet: overlay: Use the new auto network selection UI
- 9be883d garnet: init: Give proper permissions for /dev/diag
- 7994cd8 garnet: Update Axion flags

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
## 2026-09-23

### device_xiaomi_garnet

- f81c046 garnet: Update Axion flags

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
## 2026-09-15

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
## 2026-09-13

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- 06ce54a garnet: Drop 32-bit performance libraries
- f3ba795 garnet: Drop 32 Libs
- bcecc4f garnet: Restore eUICC mirilhook from 35d1c0f

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
## 2026-09-10

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

- b7421fb garnet: camera: Set torch default strength level to max
- ae555e1 garnet: props: Disable unnecessary logging
- ee48995 garnet: debloat: Drop jelly app
- eb58e1b garnet: rootdir: Use foreground cpuset/uclamp for gralloc Makes sure rendering has enough capacity.
- 4dd95bb garnet: rootdir: Use foreground uclamp for hwcomposer Matches SF, makes sure rendering always has enough capacity.
- bb82f78 garnet: props: Disable ADPF CPU hint
- 4af7ce0 garnet: audio: Route spatial output to Bluetooth
- 21aaace garnet: power: Add CPU GPU performance power hints
- 65069b7 garnet: audio: Add DSEE effect
- 470776a garnet: Remove lineage dependencies
- 438dc66 garnet: audio: Fix overly loud notification sound
- 92ce243 garnet: Implement torch light control
- 29fa733 garnet: rootdir: Don't configure zram in QCOM's init post boot script

### vendor_xiaomi_garnet

- d54f67b garnet: vendor: Set KGSL default power level
- 362183e garnet: init: Reset readahead values for 512 always
- f64a6fa garnet: Don't configure zram in post boot scripts
- 47b8cff garnet: switch to deep suspend-to-RAM
- 7a02fe8 garnet: Add missing Leica video filter
- 41ff41d garnet: add 32-bit Adreno Gpu libraries
- 30d6ab5 garnet: Update Adreno GPU V@0837.0.9 blobs
- d07ed81 garnet: tune reclaim watermark and swappiness for smoother UX

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- dcbb0fe dolby: enable UDC/AC4 software codecs
- c36a343 dolby: link blobs against v33 libstagefright_foundation
- 53c54cb dolby: Redesign UI with Material 3 Expressive colors
- 5fa80a1 dolby: Add AutoEQ headphone correction profiles contributor entry
- c9d9b8a dolby: Add persian translations
- d7c39aa dolby: Redesign main card banner with Dolby logo
- 126bd27 dolby: Add per-band fine tuner to equalizer
- 810e555 dolby: Revert offline AutoEQ and restore online profile fetching
- f81c32d dolby: Implement per-device audio memory and offline AutoEQ engine
- e854e91 dolby: Import DAX config from Sony PDX245
- dfa94d6 dolby: Add DSEE audio enhancement

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)
