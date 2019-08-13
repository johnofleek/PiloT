## tested in uPilot 

## AT Config

```
Unlock

AT!entercnd="A710"

ati9                                                                            
Manufacturer: Sierra Wireless, Incorporated                                     
Model: EM7455                                                                   
Revision: SWI9X30C_02.24.05.06 r7040 CARMD-EV-FRMWR2 2017/05/19 0

Composition

AT!usbcomp=?
!USBCOMP:                                                                       
AT!USBCOMP=<Config Index>,<Config Type>,<Interface bitmask>                     
  <Config Index>      - configuration index to which

AT!usbcomp?                                                                     
Config Index: 1                                                                 
Config Type:  1 (Generic)                                                       
Interface bitmask: 0000050D (diag,nmea,modem,rmnet0,rmnet1)

So maybe try 

AT!usbcomp=1,1,0000100D



```

