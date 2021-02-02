# UDEV - investigation
The following notes are cover an ongoing investigation into an issue with using the HL7802 with modem manager. The focus is on how to make a modem visible to modem manager probing when the modem is attached to physical interface that the OS has not marked (by default) as a modem.

The key point is that udev needs to be configured correctly for an interface that has a modem attached.


## Notes
AT+KUSBCOMP=1,1,2,3

```
1 == enable USB
1 AT
2 AT_PPP
3 NMEA
```

AT_PPP disabled on USB enabled on UART
AT+KUSBCOMP=1,1,0,3


try this text in file /etc/udev/rules.d/ttyACM1-HL7702.rules

```
ACTION=="add|change|move", KERNEL=="ttyUSB0", ENV{ID_MM_TTY_FLOW_CONTROL}="none", ENV{ID_MM_TTY_BAUDRATE}="115200", ENV{ID_MM_CANDIDATE}="1", ENV{ID_MM_DEVICE_PROCESS}="1",ENV{ID_MM_PORT_TYPE_AT_PPP}="1"
```

Other attempts
```
ACTION=="add", KERNEL=="ttyACM1", ENV{ID_MM_DEVICE_PROCESS}="1"
```

```
ACTION=="add", KERNEL="fe215040.serial", ENV{ID_MM_DEVICE_PROCESS}="1"
```


Then reboot (in my case I used "sudo udevadm trigger" as a shortcut and udevadm monitor in a different shell)

Test

pi@raspberrypi:/etc/udev/rules.d $ mmcli -L
    /org/freedesktop/ModemManager1/Modem/0 [Sierra Wireless] HL7802



From   
https://askubuntu.com/questions/740584/enabling-serial-network-devices-with-modemmanager/740585

and  

https://superuser.com/questions/1043141/configuring-a-ppp-device-with-networkmanager-nmcli

## Some practical udev debug

This is using the HL7802 USB interface - the HL7802 AT command port has been configured to appears to the RPi OS as /dev/ttyACM1
```
pi@raspberrypi:~ $ udevadm info /dev/ttyACM1
P: /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.2/tty/ttyACM1
N: ttyACM1
L: 0
S: serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.2
S: serial/by-id/usb-Altair_Semiconductor_ALT1250_IoT_V1.00-if02
E: DEVPATH=/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.2/tty/ttyACM1
E: DEVNAME=/dev/ttyACM1
E: MAJOR=166
E: MINOR=1
E: SUBSYSTEM=tty
E: USEC_INITIALIZED=6111123
E: ID_BUS=usb
E: ID_VENDOR_ID=1199
E: ID_MODEL_ID=c001
E: ID_PCI_CLASS_FROM_DATABASE=Serial bus controller
E: ID_PCI_SUBCLASS_FROM_DATABASE=USB controller
E: ID_PCI_INTERFACE_FROM_DATABASE=XHCI
E: ID_VENDOR_FROM_DATABASE=Sierra Wireless, Inc.
E: ID_MODEL_FROM_DATABASE=VL805 USB 3.0 Host Controller
E: ID_VENDOR=Altair_Semiconductor
E: ID_VENDOR_ENC=Altair\x20Semiconductor
E: ID_MODEL=ALT1250_IoT
E: ID_MODEL_ENC=ALT1250\x20IoT
E: ID_REVISION=0000
E: ID_SERIAL=Altair_Semiconductor_ALT1250_IoT_V1.00
E: ID_SERIAL_SHORT=V1.00
E: ID_TYPE=generic
E: ID_USB_INTERFACES=:020200:0a0000:
E: ID_USB_INTERFACE_NUM=02
E: ID_USB_DRIVER=cdc_acm
E: ID_USB_CLASS_FROM_DATABASE=Miscellaneous Device
E: ID_USB_PROTOCOL_FROM_DATABASE=Interface Association
E: ID_PATH=platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.2
E: ID_PATH_TAG=platform-fd500000_pcie-pci-0000_01_00_0-usb-0_1_3_1_2
E: ID_MM_CANDIDATE=1
E: DEVLINKS=/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.2 /dev/serial/by-id/usb-Altair_Semiconductor_ALT1250_IoT_V1.00-if02
E: TAGS=:systemd:
```

```
pi@raspberrypi:~ $ udevadm info  /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.2
P: /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.2
L: 0
E: DEVPATH=/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.2
E: DEVTYPE=usb_interface
E: DRIVER=cdc_acm
E: PRODUCT=1199/c001/0
E: TYPE=239/2/1
E: INTERFACE=2/2/0
E: MODALIAS=usb:v1199pC001d0000dcEFdsc02dp01ic02isc02ip00in02
E: SUBSYSTEM=usb
E: USEC_INITIALIZED=5901935
E: ID_USB_CLASS_FROM_DATABASE=Miscellaneous Device
E: ID_USB_PROTOCOL_FROM_DATABASE=Interface Association
E: ID_VENDOR_FROM_DATABASE=Sierra Wireless, Inc.
```

This case is the RPi physical UART (40W header) - it is possible to use this port with the HL7802 physical UART as an AT command port but the +CEREG / CREG GSM issue prevents modem manager working at this time.
```
udevadm info /dev/ttyS0
P: /devices/platform/soc/fe215040.serial/tty/ttyS0
N: ttyS0
L: 0
S: serial0
E: DEVPATH=/devices/platform/soc/fe215040.serial/tty/ttyS0
E: DEVNAME=/dev/ttyS0
E: MAJOR=4
E: MINOR=64
E: SUBSYSTEM=tty
E: USEC_INITIALIZED=4328449
E: ID_MM_CANDIDATE=1
E: DEVLINKS=/dev/serial0
E: TAGS=:systemd:

udevadm info /sys/devices/platform/soc/fe215040.serial/tty/ttyS0

```
