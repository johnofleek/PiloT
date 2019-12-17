---
layout: default
title: HL8548
parent: PiloT Configuration
grand_parent: PiloT
nav_order: 2
has_children: false
---

## HL8548 PiloT

## Configuration interface

Minicom terminal to HL USB serial port
```
$ sudo minicom -D /dev/ttyACM3
```
Change factory default from 0 to 2
```
AT+KUSBCOMP=2
```
This gives 5 CDC-ACM serial ports and 1x CDC-ECM Network adapter



## LEDs
Note that the LED port configuration is erased if the modem firmware is updated

The PiloT board recommended settings are as follows - the modem should be preconfigured
 like this when the PiloT board is new

### LED D6
Set LED D6 as cellular network status indicator with the following command
```
at+ksync=2,7
```

With this setting the LED D6 behaviour is as follows

1. LED PERMANENTLY OFF: Not registered / Initialization / Registration denied / no SIM card
1. LED 600 ms ON / 600ms OFF: Not registered but searching 
1. LED 75 ms ON / 3s OFF: connected to the network

### LED D5
Set LED D5 as the cellular PiloT module boot and power indicator  
```
at+kgpio=8,1
```

With this setting the LED D5 behaviour is as follows
1. If the modem is off then the LED will be OFF
1. Following modem powered off - if a power on signal is applied to the PiloT module 
the LED should momentarily flash on
1. Then the LED will be OFF
1. After the modem has booted the LED should be ON

## HL8548 and power on signal

Recommend using the power ON / OFF scripts to ensure correct state of modem operation - this will 
overide the RPi's GPIO default state which may not be a stable signal.


## Debug
```
$ lsusb
...
Bus 001 Device 010: ID 1519:0303 Comneon 
...
```
and
[capture](./capture_HL8548networkManager.md)

