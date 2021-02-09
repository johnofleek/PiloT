---
layout: default
title: HL8548
parent: PiloT Configuration
grand_parent: PiloT
nav_order: 2
has_children: false
---

## HL8548 PiloT
This page documents basic configuration of  
1. HL8548 module when fitted to a PiloT board 
2. The PiloTs' host Raspberry Pi

## Document assumptions
1. The PiloT shell scripts are installed on the host machine (RPi)
2. The PiloT + Raspberry Pi has a suitable power supply at least 2.5A 
3. Raspian / Raspberry Pi OS


## Configure HL8548 USB composition
From the host machines Linux shell - power up the PiloT using shell script.
 Note that you may need to cd to the directory which contains the shell scripts.
```
./pilotOn.sh 
```

Use Minicom as a terminal to access the HL8548 USB serial port
```
$ sudo minicom -D /dev/ttyACM3
```
Check the HL8548 is set to the factory default USB composition
```
AT+KUSBCOMP?
```
This should return a composition of 0 - if it doesn't then set the modem to 0 with the following command.

```
AT+KUSBCOMP=0
```
USB composition 0 gives 7 CDC-ACM serial ports as follows
```
7 CDC-ACM mode, (PID: 0x0020)
USB0 – AT / NMEA / modem port
USB1 – Mobile Analyzer traces port
USB2 – 3G traces port
USB3 – AT / NMEA / modem port
USB4 – AT / NMEA / modem port
USB5 – AT / NMEA / modem port
USB6 – On-chip traces port
```
With this USB configuration netwwork manager will use the PPP protocol to support an IP connection.


## PiloT LEDs
Note that the LED port configuration is erased if the modem firmware is updated

The PiloT board recommended settings are as follows - the modem should be preconfigured
 like this when the PiloT board is new

### PiloT HL8548 LED D6
Set LED D6 as cellular network status indicator with the following command
```
at+ksync=2,7
```

With this setting the LED D6 behaviour is as follows

1. LED PERMANENTLY OFF: Not registered / Initialization / Registration denied / no SIM card
1. LED 600 ms ON / 600ms OFF: Not registered but searching 
1. LED 75 ms ON / 3s OFF: connected to the network

### PiloT HL8548 LED D5
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

## Pilot power on signal
It is recommended to use the ./pilotOn.sh and ./pilotOff.sh scripts to ensure correct
 modem operation. The scripts override the RPi's GPIO default state which may
 not be stable states.

## IP connectivity
Testing has revealed issues on some networks when using when using PDP context type 
 IPV4V6 and IPV6. If users experience issues try setting the PDP context type tp "IP" (IPv4)

## Debug
Power on the PiloT ./pilotOn.sh
Check the PiloT USB serial ports are available from an RPi shell 
```
ls /dev/ttyACM*
```
7 tty ports should be visible


and
[capture](./capture_HL8548networkManager.md)

