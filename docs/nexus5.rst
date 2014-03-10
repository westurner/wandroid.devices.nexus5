## ubuntu setup
sudo apt-get install fastboot adb

## win drivers
http://forum.xda-developers.com/showthread.php?t=2513339

## backup
adb backup -system -apk -all -f backup--system-apk-all.ab

## Lock/Unlock
block=/dev/block/platform/msm_sdcc.1/by-name/misc;
offset=16400;
locked=00;
unlocked=01;
hastamper=1;
# locked
echo -ne "\x00" | \
    dd obs=1 count=1 seek=16400 of=/dev/block/platform/msm_sdcc.1/by-name/misc;
# unlocked:
echo -ne "\x01" | \
    dd obs=1 count=1 seek=16400 of=/dev/block/platform/msm_sdcc.1/by-name/misc;
# tamper:
echo -ne "\x00" | \
    dd obs=1 count=1 seek=16404 of=/dev/block/platform/msm_sdcc.1/by-name/misc;


## xposed framework
# http://xposed.info
# http://forum.xda-developers.com/showthread.php?t=1574401

# disable xposed
touch /data/data/de.robv.android.xposed.installer/conf/disabled

# undo
cp /system/bin/app_process /system/bin/app_process.xposed
cp /system/bin/app_process.orig /system/bin/app_process



## sprint field test mode
# http://forum.xda-developers.com/showthread.php?t=2524744
# info
am start -n com.lge.SprintHiddenMenu/.sprintspec.Debug
# config editor (requires MSL)
am start -n com.lge.SprintHiddenMenu/.sprintspec.Data


## return to stock
# http://forum.xda-developers.com/showthread.php?t=2513701
adb reboot-bootloader
fastboot oem device-info

## stock images
# https://developers.google.com/android/nexus/images

## ~stock google apps
# http://battledroid.org/

## How to Unlock Bootloader, Install Custom Recovery and Root
# http://forum.xda-developers.com/showthread.php?t=2507905

## Nexus 5 ROMs, MODs, Kernels, Recoveries
# http://forum.xda-developers.com/showthread.php?t=2475401

## Nexus odds-and-ends
# http://forum.xda-developers.com/showthread.php?t=2239421

## one-click nexus 5 stock restore
# http://forum.xda-developers.com/showthread.php?t=2513937

## twrp nexus 5 recovery
# http://teamw.in/project/twrp2/205

## notes
# sys/ti: 3/4
