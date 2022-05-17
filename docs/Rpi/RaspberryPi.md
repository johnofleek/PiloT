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
The following is an example where ttyAMA0 is connected to 
* 40 Way header **primary** UART GPIO 14 (transmit) and 15 (receive)
* UART0
* UART PL011

```
pi@raspberrypi:~ $ find /dev/* -type l -ls | grep "serial"
      246      0 lrwxrwxrwx   1 root     root            7 May 16 21:17 /dev/serial0 -> ttyAMA0
      221      0 lrwxrwxrwx   1 root     root            5 May 16 21:17 /dev/serial1 -> ttyS0
```


The following sections were copied from the RPi official [documentation](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-uarts)

There are two types of UART available on the Raspberry Pi - PL011 and mini UART. 

The PL011 is a capable, broadly 16550-compatible UART.

The mini UART has a reduced feature set. With limited baud settings etc


### Primary UART
On the Raspberry Pi, one UART is selected to be present on GPIO 14 (transmit) and 15 (receive) - this is the primary UART. By default, this will also be the UART on which a Linux console may be present. Note that GPIO 14 is pin 8 on the GPIO header, while GPIO 15 is pin 10.

### Secondary UART
The secondary UART is not normally present on the GPIO connector. By default, the secondary UART is connected to the Bluetooth side of the combined wireless LAN/Bluetooth controller, on models which contain this controller.


### Raspberry Pi Zero, 1, 2 and 3
The Raspberry Pi Zero, 1, 2, and 3 each contain two UARTs as follows:

| Name |	Type |
| ---- | ------- |
| UART0 | PL011 |
| UART1 |mini UART |

### Raspberry Pi 4 and 400
The Raspberry Pi 4B and 400 have an additional four PL011s, which are disabled by default:

| Name | Type |
| ---- | ----- |
| UART0 | PL011 |
| UART1 | mini UART |
| UART2 | PL011 |
| UART3 | PL011 |
| UART4 | PL011 |
| UART5 | PL011 |



### Primary and Secondary UART
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

## Disabling the Linux Serial Console
By default, the primary UART is assigned to the Linux console. If you wish to use the primary UART for other purposes, you must reconfigure Raspberry Pi OS.
 This can be done by using raspi-config:

```
Start raspi-config: sudo raspi-config.

Select option 3 - Interface Options.

Select option P6 - Serial Port.

At the prompt Would you like a login shell to be accessible over serial? answer 'No'

At the prompt Would you like the serial port hardware to be enabled? answer 'Yes'

Exit raspi-config and reboot the Raspberry Pi for changes to take effect.
```

## UARTs and Device Tree
Various UART Device Tree overlay definitions can be found in the [kernel GitHub tree](https://github.com/raspberrypi/linux)
 The two most useful overlays are disable-bt and miniuart-bt.

disable-bt disables the Bluetooth device and makes the first PL011 (UART0) the primary UART. 

You must also disable the system service that initialises the modem, so it does not connect to the UART, using sudo systemctl disable hciuart.

You add a line to the config.txt file to apply a Device Tree overlay. Note that the -overlay.dts part of the filename is removed. For example:

dtoverlay=disable-bt
