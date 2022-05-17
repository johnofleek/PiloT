---
layout: default
title: Raspberry Pi

has_children: true
has_toc: false
---

# Purpose

Capture notes on Raspberry Pi related information related to integrating the PiloT PCA.

# Development kit
* RPi4
* Raspbian based on Bullseye

# Physical UART(s) / serial ports
http://raspberrypi.org/documentation/configuration/uart.md


# RPi Hardware UARTs


## Check current config
The following is an example where 
```
pi@raspberrypi:~ $ find /dev/* -type l -ls | grep "serial"
      246      0 lrwxrwxrwx   1 root     root            7 May 16 21:17 /dev/serial0 -> ttyAMA0
      221      0 lrwxrwxrwx   1 root     root            5 May 16 21:17 /dev/serial1 -> ttyS0
```


## Primary UART
On the Raspberry Pi, one UART is selected to be present on GPIO 14 (transmit) and 15 (receive) - this is the primary UART. By default, this will also be the UART on which a Linux console may be present. Note that GPIO 14 is pin 8 on the GPIO header, while GPIO 15 is pin 10.

## Secondary UART
The secondary UART is not normally present on the GPIO connector. By default, the secondary UART is connected to the Bluetooth side of the combined wireless LAN/Bluetooth controller, on models which contain this controller.

Primary and Secondary UART
The following table summarises the assignment of the first two UARTs:

|  Model | first PL011 (UART0) | mini UART | 
| ------ | ------------------- | --------- |
| Raspberry Pi Zero | primary  | secondary | 
| Raspberry Pi Zero W | secondary (Bluetooth) | primary |
| Raspberry Pi 1 | primary | secondary | 
| Raspberry Pi 2 | primary | secondary |
| Raspberry Pi 3 | secondary (Bluetooth) | primary | 
| Compute Module 3 & 3+ | primary | secondary | 
| Raspberry Pi 4 | secondary (Bluetooth) | primary |

