---
layout: default
title: HL7692
parent: PiloT Configuration
grand_parent: PiloT
nav_order: 2
has_children: false
---

## RC7620 PiloT
### Version tested
```
ati9
Manufacturer: Sierra Wireless, Incorporated
Model: RC7620-1
QTI baseline: MPSS.JO.2.0.2.c1.1-00073-9607_GENNS_PACK-1.416077.1.419248.1
Revision: SWI9X07H_00.08.24.02 f90cbd jenkins 2022/03/21 03:47:54
```


## RC7620 module AT command interface

From the RPi command line (shell)


AT commands can be set from the Raspberry Pi via
1. AT commands sent from the Raspberry Pi Physical UART /dev/ttyAMA0 on the 40W header to the PiloT RC7620 physical UART 
2. AT commands sent from the Raspberry Pi Virtual USB UART /dev/ttyUSB2 to the PiloT RC7620 virtual AT command UART

For example 
```
sudo minicom -D /dev/ttyAMA0
```
or
```
sudo minicom -D /dev/ttyUSB2
```



## LEDs
The PiloT LEDs are connected to the RC7620 GPIO. The state of the LEDs 

#### LED D6
Configure the RC7620 GPIO 7 as an output
```
AT+WIOCFG=7,0
```

#### LED D5
Configure the RC7620 GPIO 7 as an output
```
AT+WIOCFG=8,0
```
Turn the LED D5 ON
```
AT
```


## RC7620 USB port composition



## RC7620 and power on signal



   
  
