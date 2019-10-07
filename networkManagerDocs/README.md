## Network manager

This section explores the use of network manager in combination with the RPi / Rasbian
 OS and the USB interface of the Pilot cellular HAT board.

Network manager can replace the functionality provided by *dhcpcd* which is installed
 by default in the current versions (2019) of Raspbian and has the advantage that it
 is able to manage celluar modems as well as the usual WiFi and Ethernet network interfaces

For a quick overview of network manager take a look at [wikipedia](https://en.wikipedia.org/wiki/NetworkManager).
 Network manager has multiple interfaces - graphical, command line and an API.
 Network manager uses another component called modem manager. Modem manager also has
 GUI, CLI and API interfaces. 

Please be aware that network manager can only manage and check the modems network connectivity, it
 cannot test if a connection will support IP traffic. To test that an IP link can transport IP an 
 external app is needed  to perform a link test.
 For example in routers this function is typically implemented in a separate 
 app that sends / receives periodic ping requests 

The method described here is experimental and has only been tested on a limited set of RPi's,
 Rasbian OS variants and Pilot variants 


The following the following USB modem connectivity has been tried
* Network manager MBIM
* Network manager PPP


## Quick start guide

Note that during the quick start installation process the Raspbian default 
 method *dhcpcd* is uninstalled and replaced by network-manager and the network manager GUI
 is installed as a replacement for the dhcpcd GUI

[Quick start guide](./Quickstart.md)


Configuring profiles for network SIMs - [examples](./simUse_info.md) 

## Pilot test records
[Pilot test records](test_configurationRecords.md)  


##  More notes
[More notes](./instructions_NetworkManagerMore.md)


## Modem manager
When Network manager is loaded it also loads modem manager.
 A command line interface mmcli is available. It is also possible to install 
 a GUI

```
$ sudo apt-get install modem-manager-gui
```

Modem manager can be used for diagnostics and also enables SMS interaction via a graphical interface

