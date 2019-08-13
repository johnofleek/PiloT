## This documents purpose 
Document methods of automatically managing the wwanX interface(s) provided by the PiloT 
HAT board when used with a Raspberry PI and Raspian

So far the following connection methods are documented
* Network manager MBIM
* Network manager PPP

## Quick start

**Load required RPi apps, update modem firmware**  

Note *The following is a general process - may need 
to be adapted to suit the particular modem fitted to the Pilot*

1. Check [to see if we tested that your Pilot / modem will work with network
 manager](./test_configurationRecords.md)
1. [Clone](./git.md#checkout) this project into your RPi
1. Install [network-manager](./instructions_howToInstall_gpioAndNetworkManager.md#install-network-manager)
1. Install [network-manager-gnome](./instructions_howToInstall_gpioAndNetworkManager.md#install-network-manager-gnome)
1. Install [minicom](./instructions_howToInstall_gpioAndNetworkManager.md#install-minicom)
1. Start a shell terminal 
   1. Hold down keys [CTRL] [ALT] T or 
   1. Use the RPi Terminal icon
1. From the terminal session - power on the Pilot (doesn't apply to uPilot)
```
./Pilot/autoPilot/pilotOn.sh
```
1. Run minicom to enable AT commands to be sent to the Pilot modem [(check the actual serial port to use)](test_configurationRecords.md)
```
sudo minicom -D /dev/ttyUSB2
```
1. Check the Pilot modems firmware version -- type 
```
ATi9
```
  1. If the modem firmware doesn't appear in [here](test_configurationRecords.md) I haven't tested it
  1. If the modem does appear in [here](test_configurationRecords.md) but the
 firmware reported is older - then update the modem firmware by connecting the 
 Pilot USB port to a Windows PC using a 
one click .exe installer from [here](https://source.sierrawireless.com/)  
1. Configure the Pilot modem as required (based on firmware identified above)
  1. [some configuration examples are here](test_configurationRecords.md)
1. Reboot the RPi

  
**Configure the cellular network connection**  
1. Power on the pilot
```
./Pilot/autoPilot/pilotOn.sh
```
1. Wait for Mobile Broadband to appear in the *network manager applet* (should be visible on the Rpi Panel)
1. Use the *network manager applet*  to configure 
your wwan0 settings such as APN / username / password etc
1. If everything is installed and configured correctly network manager should 
 connect the modem when the Mobile broadband profile you created is clicked

Note that it is possible to configure network manager to automatically start the 
mobile broadband connection on power up. This can be achieved either via the GUI

## RPi app installation instructions
[Pilot RPi GPIO scripts and install network manager](./instructions_howToInstall_gpioAndNetworkManager.md)  


## System test records

[Test records](test_configurationRecords.md)  

## Network manager 

[Further use notes](./instructions_networkManager.md#connection-start)  

