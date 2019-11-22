RPi4 USB connectors vs EM7455 M.2 uPilot 

## Check the uPilot USB connected to RPi4 Black Connector

Device 9 is the EM7455 USB 2.0
```
pi@raspberrypi:~ $ lsusb -t
/:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=dwc_otg/1p, 480M
/:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M
/:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 480M
    |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 2: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
        |__ Port 3: Dev 9, If 0, Class=Vendor Specific Class, Driver=qcserial, 480M
        |__ Port 3: Dev 9, If 2, Class=Vendor Specific Class, Driver=qcserial, 480M
        |__ Port 3: Dev 9, If 3, Class=Vendor Specific Class, Driver=qcserial, 480M
        |__ Port 3: Dev 9, If 12, Class=Communications, Driver=cdc_mbim, 480M
        |__ Port 3: Dev 9, If 13, Class=CDC Data, Driver=cdc_mbim, 480M
        |__ Port 4: Dev 4, If 0, Class=Hub, Driver=hub/4p, 480M
            |__ Port 4: Dev 5, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
            |__ Port 4: Dev 5, If 1, Class=Human Interface Device, Driver=usbhid, 1.5M
```

## Check the uPilot USB connected to RPi4 Blue Connector

Device 3 is the EM7455 USB 3.0

```
pi@raspberrypi:~ $ lsusb -t
/:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=dwc_otg/1p, 480M
/:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M
    |__ Port 1: Dev 3, If 0, Class=Vendor Specific Class, Driver=qcserial, 5000M
    |__ Port 1: Dev 3, If 2, Class=Vendor Specific Class, Driver=qcserial, 5000M
    |__ Port 1: Dev 3, If 3, Class=Vendor Specific Class, Driver=qcserial, 5000M
    |__ Port 1: Dev 3, If 12, Class=Communications, Driver=cdc_mbim, 5000M
    |__ Port 1: Dev 3, If 13, Class=CDC Data, Driver=cdc_mbim, 5000M
/:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 480M
    |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 2: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
        |__ Port 4: Dev 4, If 0, Class=Hub, Driver=hub/4p, 480M
            |__ Port 4: Dev 5, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
            |__ Port 4: Dev 5, If 1, Class=Human Interface Device, Driver=usbhid, 1.5M
```
From   
https://www.linux.com/learn/intro-to-linux/2017/3/deep-hardware-discovery-lshw-and-lsusb-linux  
USB versions of the connected devices  
1.5M = USB 1.1  
480M = USB 2.0  
5000M = USB 3.0  



