---
layout: default
title: EM7455
parent: Pilot Configuration
grand_parent: Pilot
nav_order: 2
has_children: false
---

## EM Board 

The following information targets the uPilot board 

## AT Config

For more details take a look at the AT command manual available on [the_source](https://source.sierrawireless.com)  

NetworkManager / ModemManager occupies and transacts on the Modem/AT serial interfaces so it is recommended to
stop their processes before sending AT commands to the modem  

Unlock  
```
AT!entercnd="A710"
```

Check modem type and firmware rev
```
ati9                                                                            
Manufacturer: Sierra Wireless, Incorporated                                     
Model: EM7455                                                                   
Revision: SWI9X30C_02.24.05.06 r7040 CARMD-EV-FRMWR2 2017/05/19 0
```

USB composition settings

```
AT!usbcomp=?
!USBCOMP:                                                                       
AT!USBCOMP=<Config Index>,<Config Type>,<Interface bitmask>                     
  <Config Index>      - configuration index to which

AT!usbcomp?                                                                     
Config Index: 1                                                                 
Config Type:  1 (Generic)                                                       
Interface bitmask: 0000050D (diag,nmea,modem,rmnet0,rmnet1)
```

Enable just MBIM 

```
AT!usbcomp=1,1,0000100D
```


## Others - untested


```
EM75xx series:
AT!ENTERCND="A710"
AT#USBCOMP=1,3,100D
AT!RESET
```
