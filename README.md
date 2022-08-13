# RespawnTimer.gtp #Project1999 #EverQuest #GINA

This GINA package can display respawn times by zone. It can also display respawn times per mob.

# How to use

## Download
Select `Download ZIP` from the green button labeled `Code` in the upper right corner of this page to download the file.
 
## Create RespawnTimer overlay

Overlays tab: Add Timer Overlays (watch icon) > change "Overlay#x" at center of window to "RespawnTimer" > Sort: Time Remaining > Save

Categories tab: Add > Name: RespawnTimer > Timers Overlay: RespawnTimer

## Install gtp files
Sharing tab > Import > From GINA Package File > `RespawnTimer.gtp` and `RespawnTimeDB.gtp`

## Config
Select the character in the pane on the left side of `GINA` and check the checkbox at the top of the `Respawn Time DB` tree.
Leave the `Respawn Timer` unchecked for now.

## Start camp
When you zone or run the `/` or `/who` command, the respawn time for the zone you are in is displayed as a timer.
Find that time in the `Respawn Timer` tree and check it. As you kill mobs, the respawn time for each mob will line up.

```
A Death Beetle
^^^^^
```

Two timers appear when you kill a mob. The timer in the name of the mob uses slain logs. It is only valid for tanks and melees, as it only appears when you are near them when you kill them.
The second timer uses the xp log, and this log does not show what it killed. However, the xp log is helpful to chain pullers because it reaches a wide area.

# Advance

## memo
For example, if you want to make a note of a nasty mob PH that has a slightly different respawn time.
```
/em ##freeti
```

## reset
If you want to erase all timers when moving to another camp.
```
/em ##reset
```

## add manually
For example, if you are med at a distance where slain cannot pick up and do not want to move.
```
/em ## %t
```
Note the space before the %. Without it, the % macro will not expand.

## Feedback
Please feel free to contact me for corrections and bug reports.
tell nekomimi, nagatoyuki, chomusuke on green or DM to pero#8035.
