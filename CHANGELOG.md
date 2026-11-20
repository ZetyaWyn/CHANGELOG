# Changelog

## 2026-11-20

### device_xiaomi_garnet

- 3bc68f2 garnet: props: enable display idle timers
- 92f7cae garnet: fix charge limit write failure and stop mi_thermald overriding it
- 5fea373 garnet: audio: Add ViPER4Android effect
- 1f3f338 garnet: Enable R8 optimizations for system_server and SystemUI
- ebd0842 garnet: Drop add_power_save (already set in vendor) and silence noisy log tags
- d619524 garnet: Add missing RKPD props from stock rom
- b424b99 sepolicy: Fix IMS factory hwservice declaration
- dfb2756 garnet: Drop Dolby Vision
- b9d830b garnet: Import the AIDL Codec2 video HAL from PDX257
- e793efb Revert "garnet: Move c2_manifest_vendor.xml to device tree"
- 3d8b410 Revert "garnet: configs: hidl: Switch C2 HAL to AIDL and drop unused instances"
- 6909d09 garnet: configs: hidl: Switch C2 HAL to AIDL and drop unused instances
- 09df3ca garnet: sepolicy: allow vendor_hal_usb_qti to read sysfs_udc
- 08f50ad garnet: sepolicy: hal_fingerprint: allow vendor system property access
- b6d33c1 garnet: sepolicy: hal_fingerprint: allow map of vendor_system_prop
- cd3c35b garnet: sepolicy: Update alarm AIDL service

### vendor_xiaomi_garnet

- 12e26fd vendor: garnet: Allow undefined symbols in adpl and netmgrd
- 1038026 garnet: Route the camera.qcom.so CamX format lookup through the shim
- 4fff96d garnet: Use the stock display ids for the display configs
- a3604d4 garnet: Import the AIDL Codec2 video HAL from PDX257
- 74580da garnet: Link the legacy CamX JPEG override shim
- 64fb7bb garnet: Import the AIDL CamX glue from PDX257
- 3e53c32 garnet: Import the stock HIDL audio userspace
- 287f3d1 garnet: Import the PAL and AGMIPC HIDL interface libraries
- 3a3cf65 garnet: Import the parrot 6.6 Adreno, FastRPC, DSP and QSPM blobs

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- f6d9229 dolby: disable volume leveler by default
- c64c931 dolby: Import DAX config from Sony PDX245
- 6bfc170 dolby: Add DSEE audio enhancement
- 2d673f1 dolby: Add contributors
- 51fb13b dolby: Simplify translation contributor definitions
- 4afd325 dolby: Add stacked animated avatars with multi-contributor support
- 66f79db dolby: Fetch contributor profile pictures from GitHub
- 19f76d6 dolby: Use 2-column grid for translation contributors
- a2f629d dolby: Add callout to contribute translations in Credits dialog
- d5ffae2 dolby: Add translation contributors to Credits dialog
- 75db21a dolby: add VINTF manifest and framework compatibility matrix
- c31e60c dolby: DSPVolumeSynchronizer: Migrate to `privapp_allowlist`
- f6ac0df dolby: DSPVolumeSynchronizer: Add icon
- d66d808 dolby: Implement DSPVolumeSynchronizer
- 7626929 dolby: update dax profiles and codec capabilities
- 91d8473 dolby: use stock dolby vision cfg
- 89bc96b dolby: Apply Dolby profiles only to compatible audio routes.
- 577722b dolby: Implement AutoEQ headphone correction profiles
- 339a0ee dolby: sepolicy: allow hal_dms_default to access vendor_audio_prop
- efc50d6 dolby: Implement swipe navigation between main screens
- 0d36cc6 dolby: Use CLICK haptic instead of DOUBLE_CLICK
- bb21749 Dolby: Enable R8 optimization
- 1a98278 Updated Polish translation
- f35a71e dolby: Check and dismiss notification listener card if perm granted
- 9a0c318 dolby: Patch libdolbyvision.so to allocate GraphicBuffer with new size
- 41a614b dolby: Add support for Dolby Vision
- d3d4698 Add device state memory strings for Indonesian localization
- 915dd1b Add device state memory strings for Turkish localization
- ea92cfd Add device state memory strings for Russian localization
- b13a6de dolby: Make per-device audio memory configurable
- b54f476 dolby: Fix permission issue
- 66d50f7 dolby: Add per-device Dolby state memory
- 9bf4f70 dolby: Add Turkish translation
- 744cbcc dolby: Update Traditional Chinese translations
- 91ebf26 dolby: Add Traditional Chinese translations
- e762cbc Move Polish translation to correct directory
- 7b77bba dolby: Add Polish translation
- 5751b72 dolby: Add `privapp-permissions-dolby.xml` as a dependency
- f822efa dolby: Whitelist permissions for Dolby
- 32de95a dolby: Add Indonesian localization
- 6186f5c dolby: Implement bottom gradient scrim
- f66f789 dolby: Move Per-app audio profile to home settings
- 2293d61 dolby: Switch to toobar instead of navbar
- fe13dd0 dolby: added ru localization
- 1ae3628 Revert "dolby: add missing software codec Attribute"
- 42713b2 update dax
- 2e93338 dolby: Separate volume leveler from audio tuning
- 937c72b dolby: Introduce mid-frequency enhancer
- db428b0 dolby: replace legacy Divider with Material3 HorizontalDivider
- 902be88 dolby: Fix profile and settings restore after audio focus loss
- d270043 dolby: Externalize UI strings for localization support
- 1c95d23 dolby: Allow hal_dms_default to connect to property socket
- ab62d09 dolby: Prevent profile reset in AppProfileMonitorService
- f45d145 dolby: Simple name better
- 9eca7b7 dolby: Add Credits & Contributors dialog
- 27d05ea dolby: Use accent color for dolby icon bg
- 2d7841a dolby: Switch to material 3 expressive color specs
- cff900e dolby: Add delete option for presets in import/export menu
- bdef22c dolby: Fix preset not loading with its original band mode
- 579260b dolby: Fix volume leveler not reading config
- 68054a8 dolby: Move notification listener permission card to home screen
- 7d314c2 dolby: Restore all profile settings on device boot
- 4f80cbb dolby: Fix navbar style
- 11a8adb dolby: Add headphone-only mode for per-app audio profiles
- acc1f1a dolby: Saftey threads and memory leak fix
- 01eeebb dolby: Add lifecycle management and resource cleanup
- b5d693a dolby: Implement Notification Listener for always-on Dolby service
- 9889109 dolby: Remove legacy vibrator fallback check
- 5c0b025 dolby: Use Material 3 Expressive motion specs
- fd516e5 dolby: Fix background color in light mode
- 278b17e dolby: Fix Band mode compatibility and array bounds crashes
- 95281a5 dolby: Prevent editing presets with mismatched band modes
- f64689f dolby: Fix bottom navbar overlap issue
- 700575a dolby: Add tile squish effect
- 96341f3 dolby: Enhance Switch UI with animated icons
- b906be3 dolby: Use neutral color for settings bg
- ecd925b dolby: Remove unnecessary GZIP compression from preset import/export
- 9c334b7 dolby: Add missing icon for Preset and Equalizer View
- 6aebff8 dolby: Extend equalizer frequency range and add configurable band modes
- eeb104f dolby: Introduce preset import/export support
- c4c5668 dolby: Implement haptic feedback
- 0d664c2 dolby: Only show toast for apps with assigned profiles
- 9481b3b dolby: Implement per-app profile management
- 873fdd3 dolby: Add 3 new profiles
- f2c74ae dolby: Fix preset now switching when switch profile
- 28ec608 dolby: Update Dolby icon
- d0e960b dolby: Fix equ curve bright bg color
- a318b22 dolby: Add view mode toggle for equalizer interface
- c39a6ae dolby: Improve equalizer curve touch responsiveness
- 267c2fa dolby: Fix equalizer preset detection and matching
- 3aa7258 dolby: Improve bottom navbar design
- ed4b480 dolby: Dynamic tile and switch shape
- be2b3ef dolby: Fix equ interface
- 9bba67c dolby: Redesign dolby interface
- 5c91dcd dolby: Add Carousel Profile Selector
- 0bdd102 dolby: Added border stroke to selected profile option
- bc8daa9 dolby: Switch to interactive frequency response curve
- 3b85fb2 dolby: add selectable bass curves and curve-based EQ processing
- 32b1e6a dolby: enhance audio controls with treble tuning
- c0e14ef dolby: add new EQ presets and extend gain range to ±15dB
- 336e88e dolby: Add bass control slider
- 5db10db dolby: Complete rewrite DolbyManager in Jetpack Compose Signed-off-by: Ghosuto <clash.raja10@gmail.com> Signed-off-by: Pabloescobar-reborn <pabloescobarreborn07@gmail.com>
- 13c32ef dolby: Use new material expressive design for settings preferences
- 0e03fff dolby: add missing software codec Attribute
- fe94e80 Merge pull request #1 from DqrKnzx/16
- 944a468 dolby: fix attributes and tags in dax_default.xml
- 63bcd89 dolby: fixup voice profile
- de23ccc dolby: update `dax-default.xml`
- 088743a dolby: Do not conditionally disable prefs on speaker
- 0353d1e dolby: Allow force disabling volume leveler
- fbb15cb dolby: Avoid hardcoded strings for custom preset
- 67eed6a dolby: Move to device encrypted storage
- 40fe685 dolby: Move effect strength settings to sliders
- 60ed7e0 dolby: Hide advanced settings in dynamic profile
- 858790d dolby: Add a menu button to reset all profiles
- 31d7175 fixup! dolby: Add intelligent equalizer setting
- d40e763 fixup! dolby: Use index of value for selecting ieq icon
- 4920046 dolby: Fix compilation error in TooltipIconButton
- c3f3a11 dolby: Use index of value for selecting ieq icon
- 753b34e dolby: Allow disabling stereo widening levels
- 05ca7c6 dolby: Enable bass enhancer on loudspeaker too
- a4cd52a dolby: Properly update profile preference summary
- b8e001e dolby: Add support for `Custom` profile
- 440bb65 dolby: Update EqualizerScreen background color for 15
- b27a259 dolby: Remove deprecated PlainTooltipBox
- d43556f dolby: Fix build with kotlinc 1.9.0
- 9390884 dolby: Convert to SwitchPreferenceCompat
- 600851e dolby: Migrate to CompoundButton.OnCheckedChangeListener
- ca33c4d dolby: Replace widget.R with collapsingtoolbar.R
- 6db983a dolby: Make sure to persist value after toggling QS tile
- 318f0ea dolby: Add intelligent equalizer setting
- b44187e dolby: Introduce graphical equalizer
- 14efd18 dolby: Add launcher icon
- 4f1393f fixup! dolby: Restore all settings upon bootup
- 4774c82 dolby: Restore current profile _after_ resetting profiles
- 7a1ef57 dolby: Do not set volume leveler amount
- e92669b dolby: Restore all settings upon bootup
- 586755d dolby: Rewrite in Kotlin
- 863fce3 dolby: Revert "Re-enable speaker virtualization after bootup"
- 5ab1d96 dolby: Introduce Dolby Atmos
- 1d06c0b dolby: Yeet Motorola Dolby Interface
- 708a47b dolby: Update readme
- 892caad dolby: Switch to AOSPA Dolby Atmos
- 6b1bb6b dolby: Create missing dolby related directory
- 0475f7e FCM: moved to dt to fix kernel target issue
- 0e837f8 Revert "dolby: Implement DSPVolumeSynchronizer"
- 263ba11 dolby: Rework on dax-default
- 54da022 dolby: configs: Rework on dax-default
- 4f911dd dolby: Update MotoDolbyDax3.apk [White icon]
- a4f8660 dolby: Patch vendor.dolby.media.c2@1.0-service with libshim_dolby
- 187c007 dolby: configs: Enable ac4
- e2df31f dolby: Enable ELF checks for libspatialaudio
- 10d3ac3 dolby: Link dolby blobs against v33 libstagefright_foundation
- 0ea2536 dolby: configs: Kang dax-default from https://github.com/reiryuki/Dolby-Atmos-Spatial-Sound-Moto-Edge-30-Ultra-Magisk-Module
- 8995c02 dolby: Kang daxService.apk and MotoDolbyDax3.apk
- 1c967d1 dolby: permissions: Kang privapp-com.motorola.dolby.dolbyui.xml
- 82e51d2 dolby: Switch to Motorola Dolby Interface
- 70b6398 Update README.mkdn
- 1e8125a dolby: Add AIDL c2 dolby instance to framework matrix
- 312f3f0 dolby: sepolicy: Add vendor_dolbyv_prop
- 2ac3634 dolby: Add xiaomi param storage libs for libhwdap
- 6e315f8 dolby: Drop 32-bit prebuilts
- 5855846 dolby: Update to Lunaris Dolby and fix DSPVolumeSynchronizer Memory leak
- a9794e1 dolby: Update Dolby configuration and remove DAX apps
- 6b61f7c dolby: Link source build AIDL dependencies with `vendor.dolby.media.c2@1.0-service`
- 4276d77 dolby: Link source build AIDL dependencies with dolby vision
- 0dd9424 dolby: sepolicy: Add AIDL rules
- 0b25943 dolby: Link Dolby vision stack with AIDL prebuilts
- 7e8628e dolby: Import AIDL prebuilts and Link with c2 Dolby
- 6126d4e dolby: Link libswdap and libdlbvol with libspatializerparamstorage
- 3a889ec dolby: Move Spatial props to system_ext
- 7830b26 dolby: Update Dolby volume listener stack
- 866ffbf dolby: Add Standalone Dolby Spatial Audio support
- f005578 dolby: sepolicy: Initial rules for DVS
- 01be966 dolby: Add Dolby vision Service support
- 934cf7a dolby: Switch to Newer Standalone Dolby Vision Stack taken from A16
- 918e361 dolby: Move Spatial props to vendor
- ef03145 dolby: Forcefully Enable bass-enhancer
- 4ad088a dolby: Update Dolby Vision stack from a
- 8066a14 dolby: Update dolby vision decoders
- d34d0a6 dolby: Add dolby vision decoders
- a1b77fa dolby: Fixup dolby c2 for Dolby Vision
- a57aa6c dolby: Fixup dax-default-spatializer.xml path
- bead24a dolby: Update readme For Spatial Audio
- 6dc6350 dolby: Import dax-default's from Motorola
- ebf34ff dolby: Update dolby blobs from pdx237
- 29de722 dolby: Set compatibility matrix version 4.0 > 1.0
- d1202ad dolby: Upgrade to Newer Sony Dolby Atoms Stack
- f0ef195 dolby: Move manifest to blueprint
- eec34ea dolby: Switch to OnePlus Interface

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-19

### device_xiaomi_garnet

- f20a9f8 garnet: BoardConfig: drop libion include and rmnetctl soong config for A16

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


## 2026-11-18

### device_xiaomi_garnet

- 631d580 garnet: props: Select AIDL for Codec2 HAL
- 5c01210 garnet: Route the camera.qcom.so CamX format lookup through the shim
- 7ee37f9 garnet: Declare the HIDL gralloc 4.0 mapper
- 6850ead garnet: modules: Load mi_thermal_interface
- 4c38794 garnet: modules: Load qti_battery_charger_main
- d7bb1b6 garnet: Use the stock display ids for the display configs
- 80688e0 garnet: Keep unused clocks and power domains enabled
- 1ca5e8a garnet: Build and load the NXP NFC driver
- 150fbdd garnet: sepolicy: Let the camera provider use QSPM
- 3195be5 garnet: sepolicy: Resolve the sm8750 neverallows
- ad38b8a garnet: udfps: Use the local HBM sysfs nodes of the display driver
- c8afd72 garnet: sepolicy: Label the panel cell id and panel info nodes
- 994eca7 garnet: Link the legacy CamX JPEG override shim
- 602425c garnet: Import the AIDL CamX glue from PDX257
- 5720246 garnet: Load the FourSemi fs19xx amplifier module
- 20eb02e garnet: Load the garnet Goodix touch driver
- dea112a garnet: Load the TIPC module
- 285c7b1 garnet: sepolicy: Import the AGMIPC service domain
- 33a44bf garnet: Import the stock HIDL audio userspace
- d7dc38b garnet: sepolicy: Import the sm8750 HIDL compat policy
- c46ed6b garnet: Import the parrot 6.6 FastRPC, DSP and QSPM setup
- 3e205c7 garnet: Load the Xiaomi hwid module in first stage
- 916fbcd garnet: Import the parrot 6.6 display HALs
- 2e0497d garnet: Save the boot logs in the oops and minidump partitions
- 95a032a garnet: Honor Xiaomi CamX stream format overrides
- 92bc986 garnet: Provide the legacy CamX JPEG override symbol
- c6fc5a9 Welcome to 6.6
- 264a56d garnet: Adapt for universal tree
- 2ec3727 garnet: power: tune powerhint for battery

### vendor_xiaomi_garnet

- 4c78d34 garnet: Import the parrot 6.6 display blobs
- 66fde04 garnet: Initial 6.6

### device_xiaomi_garnet-miuicamera

- 48d41d8 Update MIUI Gallery and MediaEditor permissions
- d1faacd Add permissions
- fa53b26 garnet: Add MiScanner

### vendor_xiaomi_garnet-miuicamera

- 3c45191 Add MIUI Scanner, Gallery and Editor

### hardware_dolby

- No new commits.

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-17

### device_xiaomi_garnet

- f294fef garnet: Increase priority of OpenDeltaOverlayGarnet
- ed4f2ac garnet: Support A/B perf mode

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


## 2026-11-16

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- 2d5b2d9 dolby: add codec2 dolby hevc encoder blobs

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-15

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- fe08c55 dolby: DSPVolumeSynchronizer: Fix receiver lifecycle, route-change volume sync, and boot permissions
- 7f53439 dolby: Update README with Sony DSEE HX and ViPER4Android references
- dab8b28 dolby: Add ViPER FX library
- 3cbd849 dolby: ViperFX-style advanced settings,Digital Sound Enhancement Engine HX and ViPER effect backend
- d1359c7 dolby: Fix per-device memory snapshots, Advanced settings state sync, and session rebinding
- 45f82c8 DSPVolumeSynchronizer: Fix receiver lifecycle, route-change volume sync, and boot permissions

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-14

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- 9b4dc5e dolby: Translations from Crowdin
- 72cda79 dolby: fix boot activation, double-tap enable, tile/card sync and profile-switch effect loss
- 19fa853 dolby: Finalize ViPER DSP, DSEE HX, single-tap UI, profile switch rebinding, and boot persistence
- 14b975e dolby: Fix Speaker optimization layout/dispatch, single-tap UI state sync, and profile switch effect rebinding
- 7418839 dolby: Fix single-tap main switch/QS sync, immediate profile effect binding, and remove DSEE logs
- 28c85a7 dolby: Add mode-specific ViPER summaries, fix Subwoofer Hz dispatch, and add DSEE HAL diagnostics
- dbd94c2 dolby: Fix bass single-tap toggles, active profile sync, subwoofer Hz slider, and compact Speaker optimization/DSEE UI
- dfcbe35 dolby: Fix ViPER Clarity toggle, SpeakerCorrection command ID, and DynamicSystem coefficients
- 7bd6540 dolby: Add DSEE HX toggle, native SpeakerCorrection, and refine DynamicSystem DSP
- 96bfce2 dolby: Fix jni_headers include and masterEnabled parameter name
- ef4a4f3 dolby: Integrate native ViPER DSP effects and JNI engine bridge
- d4ba771 dolby: expandable rows for mid enhancer, speaker correction, volume leveler, 3D sound and dialogue enhancer

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-13

### device_xiaomi_garnet

- No new commits.

### vendor_xiaomi_garnet

- No new commits.

### device_xiaomi_garnet-miuicamera

- No new commits.

### vendor_xiaomi_garnet-miuicamera

- No new commits.

### hardware_dolby

- f1144e6 dolby: Improve ViPER effects and dynamic system
- 1e36391 dolby: ViperFX-style advanced settings backed by the ViPER effect
- dc20d7c dolby: restore EQ on bass/treble off, sync main card with QS tile
- 44b325e dolby: keep DAX XML values for profile settings the user never changed
- 2bcfe98 dolby: speaker correction on/off switch, exact EQ restore
- d5482c5 dolby: Add ViPER speaker correction
- ea24cc3 dolby: make Atmos ring draggable with spring-back
- f6c5623 dolby: fix master switch off after reboot, add bass cutoff
- 0454d79 dolby: new Atmos card with animated ring
- d65b1d3 dolby: add ViPER bass and clarity modes
- ad947a4 dolby: model ViPER bass and clarity effects on the GEQ
- 0b13258 dolby: Use foreground uclamp for Codec2 service

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-12

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

- c2b8e63 dolby: uwu

### Kernel

- [android_kernel_xiaomi_sm7435](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435/commits/16.2/)

### Kernel Modules

- [android_kernel_xiaomi_sm7435-modules](https://github.com/project-sm7435/android_kernel_xiaomi_sm7435-modules/commits/lineage-23.2/)


## 2026-11-10

### device_xiaomi_garnet

- d260e0e garnet: Prefer HW codecs for video thumbnails

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
