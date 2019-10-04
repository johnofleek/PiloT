## Quick start guide - network manager GUI

This method uses network managers GUI [NetworkManager Applet] to configure and monitor the Pilot
Cellular networking RPi HAT and it therefore requires a standard Raspian desktop install.

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
