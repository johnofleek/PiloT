---
permalink: /
layout: default
title: PiloT
nav_order: 1
has_children: true
has_toc: false
---

## Table of contents
{: .no_toc  }

{:toc}


## Summary

The PiloT is a Raspberry Pi \(RPi\) HAT compliant board which provides cellular
 connectivity, some variants also have GNSS location capability.

The PiloT power state is controlled via the Rpi GPIO and the PiloT is powered
 via the RPi 40 pin header.

Control and data communications between the PiloT with the RPi is via USB or
 the RPi physical serial port. Note that some RPi variants use the physical serial
 port to communicate with the RPi on board WiFi / Bluetooth systems. 

## Technical information links

Click [Network manager documentation](./docs/networkManagerDocs/networkManagerIndex) for
 information on an alternative method of automating PiloT cellular IP
  connectivity. Network manager also provide an developers with API's for 
  networking control, cellular SMS and general radio information.   
  
Click [Shell Scripts](./scripts_pilotControl/) for example scripts that
 power up and down the PiloT HAT.

Click [IP link check automation](./scripts_python_checkIp/) for a demo 
 project which adds IP ping link checking to the RPi.
 
Click [Speed tests](./speedtests/README.md) for records of practical
 network speed testing.

## Compatibility

Raspberry Pi 4 Model B  - with upgrade to wiring pi - [here](http://wiringpi.com/wiringpi-updated-to-2-52-for-the-raspberry-pi-4b/)  
Raspberry Pi 3 Model B+  
Raspberry Pi 3 Model B  
Raspberry Pi 2 Model B  
Raspberry Pi Zero W  
Raspberry Pi Zero  

  

![Picture of PiloT_should appear here alt <](./images/PilotPCA.png "PiloT")


