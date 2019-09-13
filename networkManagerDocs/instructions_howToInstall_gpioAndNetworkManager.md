# Install useful stuff
* RPi GPIO control for Pilot HAT board
* Network manager - enables control and automation of the Pilot Modem


## Pilot GPIO control lines

RPi GPIO lines are used to control the modules *power supply* and also the modules *ON* signal. 
Two scripts have been created - they use the RPi builtin wiringPi application 

* pilotOn.sh
* pilotOff.sh

Install the scripts by cloning this project from github onto the RPi [like this -- github "checkout"](./git.md)  

To power up the Pilot module
```
cd to correct folder
./pilotOn.sh
```

To power down the Pilot module
```
./pilotOff.sh
```

### Use of raspbian built in wiringPi RPi4  -- update the wiringPi app

At the time of writing (August 2019) the builtin wiringPi app doesn't work on the RPi4  
This is a workaround from wiringpi.com

To upgrade:
```
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
```

Check with:
```
gpio -v
```



## Install network-manager
NetworkManager is a linux daemon  

> The NetworkManager daemon attempts to make networking configuration and operation as
 painless and automatic as possible by managing the primary network connection and
 other network interfaces, like Ethernet, Wi-Fi, and Mobile Broadband devices. 
 NetworkManager will connect any network device when a connection for that device
 becomes available, unless that behavior is disabled. Information about networking is
 exported via a D-Bus interface to any interested application, providing a rich API
 with which to inspect and control network settings and operation.


[For more info](https://developer.gnome.org/NetworkManager/stable/NetworkManager.html)

```
sudo apt-get install network-manager
```

The following command line apps are available
* nmcli
* nmtui


## Install network-manager-gnome 


```
sudo apt-get install network-manager-gnome
```
The following autoruns on startup providing a graphical user interface that can be
 used to configure network manager
* NetworkManager Applet

Reboot

## Install minicom
sudo apt-get install minicom 





