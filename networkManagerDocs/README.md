## This documents purpose 
Documents a method of automatically managing network interfaces with 
[network manager](https://developer.gnome.org/NetworkManager/stable/NetworkManager.html),
 including the cellular wwanX 
 interface(s) provided by the PiloT HAT board, when used with a Raspberry PI and Raspian.

At this time it is experimental and has only been tested on a limited set of RPi
, Rasbian OS variants and Pilot variants 

Note that by following the installation process below the Raspbian default network manager
 method *dhcpcd* will be replaced with network-manager and that if the network manager GUI
 is installed it will replace the dhcpcd GUI

So far the following modem network interface technologies have been tried
* Network manager MBIM
* Network manager PPP

## Quick start
This method uses network managers GUI [NetworkManager Applet] to configure and monitor the Pilot
Cellular networking RPi HAT and it therefore requires a standard Raspian desktop install

*Notes*  
1. The following is a general process it may need 
to be adapted to suit the particular modem fitted to the Pilot
2. Not all combinations of Pilot / RPi / Rasbian OS have been tested  
3. How to start a shell terminal
   1. Hold down keys [CTRL] [ALT] T or 
   1. Use the RPi Terminal icon
4. At the time of writting the shell scripts below (.sh) are in this folder ~/Pilot/scripts_pilotControl/



**Power up the Pilot / modem**  
1. Clone [this](./git.md#checkout) project into your RPi (using a shell terminal)
   ```
   git clone http://github.com/johnofleek/Pilot
   ```
1. Install text-based modem control and terminal emulation  application [minicom](./instructions_howToInstall_gpioAndNetworkManager.md#install-minicom)
   ```
   sudo apt-get install minicom
   ```
1. From a shell terminal - power on the Pilot using a convenient script (doesn't apply to uPilot)
   ```
   ./pilotOn.sh
   
   ```
   If this script fails to power up the Pilot - check that the wiringPi version installed on
    on your RPi Raspian is compatible with the RPi hardware in use. For example at the time
    of writing the RPi4 HW needs an updated wiringPi install   

1. For information on your Pilot's LED behaviour click [LED behaviour](#pilot-modem-configuration-notes)
   and follow the links

**Pilot / modem configuration**  
1. To enable AT commands to be sent to the Pilot modem - run minicom [(check the actual serial port to use)](test_configurationRecords.md)
   ```
   sudo minicom -D /dev/ttyACM0
   ```
1. Check the Pilot modems firmware version -- type AT command
   ```
   ATi9
   ```

   1. If the modem firmware reported doesn't appear in [here](test_configurationRecords.md) we haven't 
      tested it
   1. If the modem does appear in [here](test_configurationRecords.md) but the
      firmware reported is older - then update the modem firmware by connecting the 
      Pilot USB port to a Windows PC and use a 
      one click .exe installer from [here](https://source.sierrawireless.com/) to install updated firmware
      into the Pilot modem
   1. If your RPi variant doesn't appear [here](test_configurationRecords.md) I haven't tested it
   1. If your Raspian variant doesn't appear [here](test_configurationRecords.md) I haven't tested it
1. Configure the Pilot modem as required (based on firmware identified above)
   1. [Some configuration examples are here](test_configurationRecords.md)
   1. Pay particular attention to the usb composition setting - if in doubt check the 
      AT command manual for the particular modem that is being used - a composition with an MBIM setting is 
      recommended
1. [Check](./test_configurationRecords.md) to see if we tested your Rpi / Raspbian OS will work with network
 manager
1. Power down the Pilot HAT - run the following script
   ```
   ./pilotOff.sh
   ```
1. Reboot the RPi


**Install required RPi apps**  
1. Power down the Pilot HAT
   ```
   ./pilotOff.sh
   ```
1. Install [network-manager](./instructions_howToInstall_gpioAndNetworkManager.md#install-network-manager)
   ```
   sudo apt-get install network-manager
   ```

1. Install the GUI [network-manager-gnome](./instructions_howToInstall_gpioAndNetworkManager.md#install-network-manager-gnome)
   ```
   sudo apt-get install network-manager-gnome
   ```


**Uninstall RPi apps not required**

1. Remove openresolv and dhcpcd as they interfere with the operation of network manager
   ```
   sudo apt purge openresolv dhcpcd5
   ```
1. Reboot the RPi


  
**Configure the cellular network connection**  
1. From a shell terminal - power on the Pilot
   ```
   ./pilotOn.sh
   ```
1. Wait for Mobile Broadband to appear in the *network manager applet* (should be visible on the Rpi Panel)
1. Use the *network manager applet*  to configure 
your wwan0 settings such as APN / username / password etc
1. If everything is installed and configured correctly network manager should 
 connect the modem using the Mobile broadband profile you created is clicked
1. To power down the Pilot run the following script
   ```
   ./pilotOff.sh
   ```

### Further network manager notes
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



## Network manager 
Network manager has multiple user interfaces
* Command line - nmcli
* Gui - NetworkManager Applet
* API

[Further use notes](./instructions_networkManager.md#connection-start)  

## Modem manager

When Network manager is loaded it also loads modem manager.
 A command line interface mmcli is available. It is also possible to install 
 a GUI

```
$ sudo apt-get install modem-manager-gui
```

Modem manager can be used for diagnostic and also to SMS interaction

