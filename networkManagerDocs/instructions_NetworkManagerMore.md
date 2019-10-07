## Network manager and general notes


## Use of raspbian built in wiringPi RPi4  -- update the wiringPi app

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


## NetworkManager
NetworkManager is a linux daemon - from the manual  

 The NetworkManager daemon attempts to make networking configuration and operation as
 painless and automatic as possible by managing the primary network connection and
 other network interfaces, like Ethernet, Wi-Fi, and Mobile Broadband devices. 
 NetworkManager will connect any network device when a connection for that device
 becomes available, unless that behavior is disabled. Information about networking is
 exported via a D-Bus interface to any interested application, providing a rich API
 with which to inspect and control network settings and operation.


Use Linux network manager to provide automatation of the Pilot cellular modules 
IP interface bringup in Linux

[For more info](https://developer.gnome.org/NetworkManager/stable/NetworkManager.html)

[Documentation on network Manager](https://wiki.debian.org/NetworkManager)  

[Documentation on network manager cellular command line configuration](https://docs.ubuntu.com/core/en/stacks/network/network-manager/docs/configure-cellular-connections)


### NetworkManager - configuration 
NetworkManager can be configured in a few different ways    
* GUI
* nmcli
* nmtui
* direct data file edit
* API

Note that the graphical interface has a database of general cellular networks.  
To configure network manager manually use nmcli or manually edit the files on the RPi system - 
for example to change the APN / add PAP / CHAP / USER / PASSWORD ...  
  

### NetworkManager - autoconnect 

The network interface can be set to autoconnect when the cellular module is on - if the connection configuration has setting   
```
autoconnect=true
```



### NetworkManager - configure autoconnect using nmcli

Make the change - example
```
pi@raspberrypi:~ $ sudo nmcli c modify '3 Internet' connection.autoconnect yes
```

Check the result
```
pi@raspberrypi:~ $ nmcli c show '3 Internet' | grep connection.auto
connection.autoconnect:                 yes
connection.autoconnect-priority:        0
connection.autoconnect-retries:         -1 (default)
connection.autoconnect-slaves:          -1 (default)
```

[To list nmcli settings "show" see](./exampleNmcliConnectShow.md)

### Network manager - configure via GUI
Right click on the tray icon - "edit - connections"



### Configure manually via the file system
Configuration settings are actually stored in the file system e.g.

```
root@raspberrypi:/etc/NetworkManager# ls system-connections
'3 Internet.nmconnection'
```

[For an example see](./exampleNetworkManagerConfigFile.md)  


```
sudo service network-manager restart
```

### Stop network manager**  
```
sudo /etc/init.d/network-manager stop
```

### Restart network manager
After editing settings - the network manager daemon needs to be restarted for the changes to take effect  

```
sudo service network-manager restart
```

even better [see](https://www.freedesktop.org/wiki/Software/ModemManager/Debugging/)



## Debug stuff

**Have a look at the syslog**  
```
sudo tail -f /var/log/syslog

```



**Have a look at running processes**  
```
ps -U0 -o 'tty,pid,comm' | grep ^?
```

