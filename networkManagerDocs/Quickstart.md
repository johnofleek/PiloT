---
title: QuickStart Guide
---

This guide installs a universal IP cellular connectivity solution onto the Raspbian OS targeting the PiloT HAT board and Raspberry
PI \(RPi\) hardware.

NetWorkManager, NetworkManager GUI and ModemManager are installed onto a Raspbian OS  

NetworkManagers GUI (NetworkManager Applet) is used to configure cellular IP
 connectivity and to stop, start and monitor IP connections   

This QuickStart guide requires 
* Raspberry Pi
* Standard Raspian desktop installation ***
* Pilot board and USB cable

*** Desktop installation is required because NetworkManager GUI is used for in
 this guide because it provides a simple way to observe the system behaviour, however,
 the underlying technology will work with a non-GUI system

  
<BR>



## Power up the PiloT board  
1. Clone the project into your RPi (maybe use a shell terminal). This creates a local copy of the project which includes this documentation and any project related scripts
   ```
   git clone http://github.com/johnofleek/PiloT
   ```
   
1. Install the minicom command line terminal emulation application 
   ```
   sudo apt-get install minicom
   ```
   
1. From a shell terminal - power on the PiloT using a convenient script (doesn't apply to uPiloT)
   ```
   ./pilotOn.sh
   
   ```
   *If this script fails to power up the PiloT*  
   
   Check that the wiringPi version installed on on your RPi Raspian is compatible with the RPi hardware
   in use. For example at the time of writing the RPi4 HW needs an updated wiringPi install  

1. For information on your PiloT's LED behaviour click [LED behaviour](./instructions_modemConfiguration.md)
   and follow the links to the module fitted to your PiloT 
<BR>

## PiloT modem check and set configuration  
1. To enable AT commands to be sent to the PiloT modem - run minicom [(check the actual serial port to use)](test_configurationRecords.md) - note that if NetworkManager ModemManager is running then stop them before
trying to send commands to the modem
   ```
   sudo minicom -D /dev/ttyACM0
   ```
1. Read the PiloT modem information
   Type the following AT command into minicom - the modem will report information about itself such as it's Firmware version.
   On some modems the serial port times out when there is no activity - the first carriage return will wake the modem up
   ```
   <CR>
   ATi9<CR>
   ```
1. Check the PiloT modem information
   Only a limited number of combinations have been tried - take a look at [this](test_configurationRecords.md)
   to see what we have tested then compare this to the information obtained about the modem
    * Does the modem does appear in our record but the firmware reported is older - it's possible to  update
      the modem firmware by connecting the PiloT USB port to a Windows PC and use a one click .exe installer from
      [here](https://source.sierrawireless.com/) to install updated firmware into the PiloT modem  
    * If the reported modem type reported doesn't appear - please contact us
    * If your RPi variant doesn't appear - it might work please let us know
    * If your Raspian variant doesn't appear - it might work please let us know
    * If we tested your PiloT has been tested with NetworkManager
    
1. Configure the PiloT modem as required (based on firmware identified above)
   * Carry out the modem specific configuration [instructions](instructions_modemConfiguration.md)  
     Please pay particular attention to the usb composition setting - if in doubt check the 
     AT command manual for the particular modem that is being used - if it's supported by the modem
     a composition with an MBIM setting is recommended

1. Power down the PiloT HAT by running the following script  
   ```
   ./pilotOff.sh
   ```
1. Reboot the RPi
<BR>

## Install required RPi apps  

1. Power down the PiloT HAT
   ```
   ./pilotOff.sh
   ```
1. Install network-manager
   ```
   sudo apt-get install network-manager
   ```

1. Install the GUI network-manager-gnome
   ```
   sudo apt-get install network-manager-gnome
   ```
<BR>

## Uninstall RPi apps not required

1. Remove openresolv and dhcpcd as they interfere with the operation of network manager
   ```
   sudo apt purge openresolv dhcpcd5
   ```
   It is also possible to uninstall the dhcpcd GUI as it's no longer functional
1. Reboot the RPi
<BR>

  
## Configure the cellular network connection  
1. From a shell terminal - power on the PiloT
   ```
   ./pilotOn.sh
   ```
1. Wait for Mobile Broadband to appear in the *network manager applet* (should be visible on the Rpi Panel)
1. Use the *network manager applet*  to configure 
your wwan0 settings such as APN / username / password etc - maybe some variant of these [examples](./simUse_info.md)
1. If everything is installed and configured correctly network manager should 
 connect the modem using the Mobile broadband profile you created is clicked
1. To power down the PiloT run the following script
   ```
   ./pilotOff.sh
   ```


## Assumptions and notes

* The instructions assume that the git project has been cloned into the users home directory.
  To access or run the power control scripts  
 
  ```
  cd ~/Pilot/scripts_pilotControl
  ```

* The paths used in this guide - for example **./pilotOn.sh** assumes that the user has changed
  directory to the directory which contains the pilotOn.sh script - the shell command **\[ls\]** will list
  what is available in a directory

When using the guide please consider
* Not all combinations of PiloT / RPi / Rasbian OS have been tested  
* To start a Raspbian shell terminal - hold down keys [CTRL] [ALT] T or use the RPi Terminal icon
