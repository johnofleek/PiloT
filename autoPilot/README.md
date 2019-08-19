## This documents purpose 
Documents a method of automatically managing network interfaces with 
[network manager](https://developer.gnome.org/NetworkManager/stable/NetworkManager.html),
 including the cellular wwanX 
 interface(s) provided by the PiloT HAT board, when used with a Raspberry PI and Raspian.

At this time it is experimental and has only been tested on a very limited set of RPi
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



**Power up the Pilot / modem**  
 
1. From a shell terminal - power on the Pilot using a convenient script (doesn't apply to uPilot)
   ```
   ./Pilot/autoPilot/pilotOn.sh
   ```
1. For further information on expected Pilot [LED behaviour](#pilot_modem_configuration_notes)
   

**Pilot / modem configuration**  
1. To enable AT commands to be sent to the Pilot modem - run minicom [(check the actual serial port to use)](test_configurationRecords.md)
   ```
   sudo minicom -D /dev/ttyACM0
   ```
1. Check the Pilot modems firmware version -- type AT command
   ```
   ATi9
   ```

   1. If the modem firmware reported doesn't appear in [here](test_configurationRecords.md) I haven't tested it
   1. If the modem does appear in [here](test_configurationRecords.md) but the
      firmware reported is older - then update the modem firmware by connecting the 
      Pilot USB port to a Windows PC using a 
      one click .exe installer from [here](https://source.sierrawireless.com/)   
   1. If your RPi variant doesn't appear [here](test_configurationRecords.md) I haven't tested it
   1. If your Raspian variant doesn't appear [here](test_configurationRecords.md) I haven't tested it
1. Configure the Pilot modem as required (based on firmware identified above)
   1. [Some configuration examples are here](test_configurationRecords.md)
   1. Pay particular attention to the usb composition setting - if in doubt check the 
      AT command manual for the particular modem that is being used - a composition with an MBIM setting is 
      recommended
1. Power off the Pilot HAT - run the following script
   ```
   /Pilot/autoPilot/pilotOff.sh
   ```
1. Reboot the RPi


**Install required RPi apps**  

1. Check [to see if we tested that your Pilot / modem / Rpi /  will work with network
 manager](./test_configurationRecords.md)
1. Clone [this](./git.md#checkout) project into your RPi (using a shell terminal)
   ```
   git clone http://github.com/johnofleek/Pilot
   ```

1. Install [network-manager](./instructions_howToInstall_gpioAndNetworkManager.md#install-network-manager)
   ```
   sudo apt-get install network-manager
   ```

1. Install the GUI [network-manager-gnome](./instructions_howToInstall_gpioAndNetworkManager.md#install-network-manager-gnome)
   ```
   sudo apt-get install network-manager-gnome
   ```

1. Install text-based modem control and terminal emulation  application [minicom](./instructions_howToInstall_gpioAndNetworkManager.md#install-minicom)
   ```
   sudo apt-get install minicom
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
   ./Pilot/autoPilot/pilotOn.sh
   ```
1. Wait for Mobile Broadband to appear in the *network manager applet* (should be visible on the Rpi Panel)
1. Use the *network manager applet*  to configure 
your wwan0 settings such as APN / username / password etc
1. If everything is installed and configured correctly network manager should 
 connect the modem using the Mobile broadband profile you created is clicked
1. To power down the Pilot run the following script
   ```
   /Pilot/autoPilot/pilotOff.sh
   ```

### Further network manager notes
* With dhcpcd disabled - network manager manages all of the RPi networking interfaces
 e.g. Ethernet, WiFi, Cellular ...
* Network manager profiles can be configured to automatically start the 
mobile broadband connection on power up.   
* Network manager profiles can be set to retry if a network connection is lost - however network manager 
won't test to see if the IP connection is functional. This is a task for a different tool 
* With dhcpcd uninstalled it's GUI is still visible in the Raspbian Task bar
it reports "Connection to dhcpcpd lost"   
the functionality of this GUI is replaced by the NetworkManager Applet icon  
* Configuration of the network interfaces can be via the NetworkManager Applet GUI or the command 
line "nmcli" or 
manual hacking of the config files  
* The command line tool nmtui doesn't appear to be able to edit cellular device configuration


## RPi app installation instructions
[Pilot RPi GPIO scripts and install network manager](./instructions_howToInstall_gpioAndNetworkManager.md)  


## System test records

[Test records](test_configurationRecords.md)  


##  Pilot modem configuration notes
4G LTE [EM7455](./instructions_EM7455.md)  
4G LTE [HL7692](./instructions_HL7692.md)  
3G [HL8548](./instructions_HL8548.md)  



## Network manager 

[Further use notes](./instructions_networkManager.md#connection-start)  

