---
layout: default
title: RC7620
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

For example (assumes modem physical baud rate has been set to 115200)
```
sudo minicom -D /dev/ttyAMA0 -b 115200
```
or
```
sudo minicom -D /dev/ttyUSB2
```

## IP connectivity
At the time of testing the RC7620 supported two HOST IP connection methods
1. PPP
2. RMNET 

For information how to use PPP and RC7620 see [this](https://github.com/johnofleek/RPi_SierraWireless_PPP/blob/master/README.md#rc7620-module) 


## LEDs
The PiloT LEDs are connected to the RC7620 GPIO. The state of the LEDs 

#### LED D6
Configure the RC7620 GPIO 7 as an output which sets the LED on when the PiloT is powered up
```
AT+WIOCFG=7,4,1,1
```
AT+WIOW=7,1

#### LED D5
Configure the RC7620 GPIO 7 as an output which sets the LED off when the PiloT is powered up
```
AT+WIOCFG=8,4,1,0
```
Turn the LED D5 ON
```
AT+WIOW=8,1
```


## RC7620 USB port composition
Default USB composition is 
```
diag,nmea,modem,rmnet0,ecm
```


## RC7620 PiloT power on 

See [this](https://github.com/johnofleek/PiloT/tree/master/scripts_pilotControl) 

   
  
