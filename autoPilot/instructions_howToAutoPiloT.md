# This document
instructions_howToAutoPiloT.md August 2019  

# RPi4 GPIO-- update the wiringPi app

The two scripts 
* pilotOn.sh
* pilotOff.sh

Assuming they were installed from the github then 

Turn on  
```
./Pilot/autoPilot/pilotOn.sh
```

Turn off
```
./Pilot/autoPilot/pilotOff.sh
```

Use raspbian built in wiringPi

At the time of writing (August 2019) the built in wiring app doesn't work on the RPi4  
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



# Install network-manager
```
sudo apt-get install network-manager
```

This is has command line
* nmcli
* nmtui


# Install network-manager-gnome 
```
sudo apt-get install network-manager-gnome

```



Reboot  



