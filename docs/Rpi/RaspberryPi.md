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

# ttyAMA0

## Check current config
```
pi@raspberrypi:~ $ find /dev/* -type l -ls | grep "serial"
      246      0 lrwxrwxrwx   1 root     root            7 May 16 21:17 /dev/serial0 -> ttyAMA0
      221      0 lrwxrwxrwx   1 root     root            5 May 16 21:17 /dev/serial1 -> ttyS0
```
