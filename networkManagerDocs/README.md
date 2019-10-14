## Network manager

This section explores the use of network manager in combination with the RPi
 Rasbian OS and the USB interface of the Pilot cellular HAT board.

Network manager can replace the functionality provided by *dhcpcd* which is
 installed by default in the current versions (2019) of Raspbian.
 Network manager has the advantage that it is able to automate the management
 of many cellular modems as well as managing the usual WiFi and Ethernet
 network interfaces

For a quick overview of network manager take a look at
 [wikipedia](https://en.wikipedia.org/wiki/NetworkManager).
 Network manager has multiple interfaces - graphical, command line and an API.
 Network manager uses another component called modem manager.
 Modem manager also has GUI, CLI and API interfaces. 

Please be aware that network manager can only manage and check the modems
 network connectivity, it cannot test if a network connection will support IP
 traffic. To test that the network connection can transport IP traffic an
 additional application is needed to perform a link test. For example - in routers
 the link test function is typically implemented in a separate app that sends /
 receives periodic ping requests 


## [Quickstart Guide](./Quickstart.md)

Click the heading for a quick start guide

Note that during the quick start installation process the Raspbian default 
 method *dhcpcd* is uninstalled and replaced by network-manager and the network
 manager GUI is installed as a replacement for the dhcpcd GUI

## [SIM Information](./simUse_info.md) 

Click the heading for information on our experiments configuring network manager 
 cellular profiles for different cellular operators SIMs

## [PiloT Testing Information](./test_configurationRecords.md)  

Click the heading for information on Pilot / Raspbian / RPi combinations that
 have been tried  


##  More notes

The method described in the quick start is experimental and has only been tested on
 a limited set of RPi's, Rasbian OS variants and PiloT variants  

Cellular modems which support the following connectivity methods over USB have been tried
* MBIM  
* PPP  

For [Even more notes](./instructions_NetworkManagerMore.md) 


## Modem manager

When Network manager is installed modem manager is also installed.  A command
 line interface for modemManager is available - mmcli.  It is also possible to 
 install a GUI. For example  

```
$ sudo apt-get install modem-manager-gui
```

Modem manager can be used for diagnostics and also enables SMS interaction

