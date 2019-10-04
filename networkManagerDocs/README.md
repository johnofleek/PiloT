# Network manager

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

[Quick start click](./Quickstart.md)

## Further network manager notes

* With dhcpcd disabled - network manager manages all of the RPi networking interfaces
 e.g. Ethernet, WiFi, Cellular ...
* Network manager profiles can be configured to automatically start the 
mobile broadband connection on power up.   
* Network manager profiles can be set to retry if a network connection is lost - however network manager 
won't test to see if the IP connection is functional. This is a task for a different tool - maybe read 
[this](./checkIp/README.md)
* With dhcpcd uninstalled it's GUI is still visible in the Raspbian Task bar
it reports "Connection to dhcpcd lost"   
the functionality of this GUI is replaced by the NetworkManager Applet icon  
* Configuration of the network interfaces can be via the NetworkManager Applet GUI or the command 
line "nmcli" or 
manual hacking of the config files  
* The command line tool nmtui doesn't appear to be able to edit cellular device configuration
* network manager settings are not actioned until network manager restarts - to do this manually
  ```
  sudo service network-manager restart
  ```

## RPi app installation instructions
[Pilot RPi GPIO scripts and install network manager](./instructions_howToInstall_gpioAndNetworkManager.md)  


## System test records

[Test records](test_configurationRecords.md)  


##  Pilot modem configuration notes

For documentation specific to the modem fitted to your Pilot - such as 

* Modem Configuration
* Expected LED behaviour
* Network specific information


Click the link below that matches the modem fitted to your Pilot HAT  
*If you don't know the modem type try sending AT command ATi9 to the modem via
 a command serial port*

* [EM7455](./instructions_EM7455.md) 4G/3G - supports MBIM  
* [HL7692](./instructions_HL7692.md) 4G/2G - supports MBIM  
* [HL8548](./instructions_HL8548.md) 3G/2G - PPP - possibly better to not use network manager



## Network manager - development notes

[Further use notes](./instructions_networkManager.md#connection-start)  

## Modem manager

When Network manager is loaded it also loads modem manager.
 A command line interface mmcli is available. It is also possible to install 
 a GUI

```
$ sudo apt-get install modem-manager-gui
```

Modem manager can be used for diagnostic and also to SMS interaction

