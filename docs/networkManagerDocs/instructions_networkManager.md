---
layout: default
title: Further notes 1
parent: Network Manager
nav_order: 100
has_children: false
has_toc: false
---

1. TOC
{:toc}

## Summary

In order for the cellular modem on the PiloT to be able establish a cellular IP connection, the Raspberry PI and the modem have to negotiate the connection. There are settings (APN and often a username and password) which are specific to the SIM that is fitted to the PiloT. 

The Raspberry PI needs a mechanism to control and configure the cellular modem and SIM combination.

**NetworkManager** is our recommended connection manager for the PiloT board.  
**nmcli** is our recommended network manager manual user interface tool.

The NetworkManager daemon can manage all network devices, such as Ethernet, WiFi and Mobile Broadband by using connection profiles and related command instructions such as up, down ...

There are multiple methods available to manage NetworkManager connection profiles (add / modify / delete ..) such as nmcli, nmtui, nm-applet, manually 'hacking' the connection profile with a file editor and via an API. The following is a list of the pro's and con's of the methods as noted at the time of writing (Raspbian GNU/Linux 10.6 )

| Method    | Notes |
| --------- | --- |
| nmcli     | Recommend method   |
| nmtui     | Broken for cellular (tested version)   |
| nm-applet | Defaults to using keyring for cellular connection passwords \\ <br> this doesn't play well with automation <br> The applet throws a pop up (requesting the password ) every time the modem connection starts <br> It's not available on headless systems <br> However once a connection has been configured with nmcli nm-applet works well for visualising gsm status / connecting / disconnecting profiles and it is fine for Ethernet and WiFi configuration |
| hacking connection <br> profile   | This works ok <br> but you have to be careful not to break anything 


The rest of this page details the use of command line tool **nmcli** to configure network manager connections.

The examples below were captured using an RC7xxx cellular module connected to a Raspberry pi 4 running Rasbian os 

TIPs:   
The online manuals are difficult to read and could be out of date. Sometimes it's easier to ask nmcli for help, for example "nmcli connection add --help", as it provides quite good information about the arguments required to add a new connection profile. 

However there is an issue with the nmcli local help in that the key names in the help are shortened versions of the actual key names used in the profile - leading to confusion. The reason the shortened names are acceptable is that nmcli is matching the short name to the real name. 

An example of this is gsm.user - this is documented and accepted by nmcli -  but will be displayed as gsm.username when nmcli queries the connection profile. If you manually edit the real profile only gsm.username is correct / acceptable. [list of KEYs][1.^]

To action changes to the profiles it may be necessary to restart network manager

## nmcli - exploring connection profiles

The following sections assume that
1. The PiloT board is fitted to RPi
1. A USB cable is fitted between the PiloT and RPi 
2. The PiloT is powered on - maybe use the script pilotOn.sh
3. The PiloT and RPi have a suitable External 5V PSU aim for >3A
4. A suitable SIM is fitted to the PiloT
5. This SIM is correctly orientated in the PiloT
6. The SIM has been activated and is working
7. A suitable LTE/ 3G / 2G antenna is attached to the main antenna connector
8. There is a suitable cellular signal for the chosen network

### nmcli device status

Check the connection status of the connected IP devices

For the PiloT Column TYPE will be set to **gsm**. The PiloT on test is DEVICE cfc-wdm0 the DEVICE value varies depending on the PiloT variant.

If you see TYPE gsm in this list then either the PiloT is powered up and working or you have another gsm device connected as well as the PiloT

```
pi@raspberrypi:~ $ nmcli device status
DEVICE    TYPE      STATE         CONNECTION
eth0      ethernet  connected     Wired connection 1
cdc-wdm0  gsm       disconnected  --
wlan0     wifi      disconnected  --
lo        loopback  unmanaged     --
```



### nmcli connection profiles

List all available connection profiles
Note that I had previously added connection profile "streamip" (see add below) - on a new system no gsm profiles would be visible in this list.

```
pi@raspberrypi:~ $ nmcli connection show
NAME                UUID                                  TYPE      DEVICE
Wired connection 1  5d2732bf-bd72-34a6-9f10-81ce0907f88d  ethernet  eth0
3 Internet 1        828540bb-29ed-40e5-a046-2c98e0075a91  gsm       --
streamip            f0089592-60a8-46a6-bafa-a16b4b2b13e4  gsm       --
```

### List connection profiles key value pairs

```
nmcli connection show streamip
```

The following is an edited response where the KVPs of particular cellular interest have been selected

Note in this case autoconnect has been configured to no

```
connection.id:                          streamip
...
connection.type:                        gsm
...
connection.autoconnect:                 no
connection.autoconnect-priority:        0
...
gsm.number:                             *99#
gsm.username:                           streamip
gsm.password:                           <hidden>
gsm.password-flags:                     0 (none)
gsm.apn:                                stream.co.uk
```

For interest it corresponds with the following profile stored on the RPi
```
pi@raspberrypi:~ $ sudo cat /etc/NetworkManager/system-connections/streamip.nmconnection
```

```
[connection]
id=streamip
uuid=f0089592-60a8-46a6-bafa-a16b4b2b13e4
type=gsm
autoconnect=false
permissions=user:pi:;

[gsm]
apn=stream.co.uk
number=*99#
password=streamip
username=streamip

[ipv4]
dns-search=
method=auto

[ipv6]
addr-gen-mode=stable-privacy
dns-search=
ip6-privacy=0
method=auto
```



### Add new profile "stream2"
For you particular SIM the following information is needed

| SIM information | nmcli KEY       | example nmcli VALUE |
| --------------- | ---------       | ------------- |
| apn             |  gsm.apn        | "stream.co.uk"  |
| username        |  gsm.user       | streamip |
| password        |  gsm.password   | streamip |
 

In the following example I have used the nmcli key / value pair method. On the web there are lots of alternative examples using a mixture of option / value and key / values. I have decide to standardise on key / value method because
1. it's consistent
2. it exactly matches the keys as stored in connection profiles /etc/NetworkManager/system-connections/


Create a new profile as follows  

Note the connection.interface-name ""

```
sudo nmcli connection add connection.id "A_NAME" connection.type gsm connection.interface-name "" gsm.apn "APN" gsm.username "OPTIONAL_USERNAME" gsm.password "OPTIONAL_PASSWORD"
```

Note that some SIM / APNs do not have a username and password in which case you can leave out the keys and values example below or use empty strings ""
```
sudo nmcli connection add connection.id "A_NAME" connection.type gsm connection.interface-name "" gsm.apn "APN"
```

**Example 1 - add stream SIM connection**
This is a practical example which works with my stream SIM. 

Note in the following example *connection.interface-name ""* instead of *""* we could add an interface name such as cdc-wdm0. Then we would not need to specify the name when bring a connection up. 

The reason I have used "" is that the interface name presented changes between different variants of PiloT board. An additional benefit is that we then have the option to let nmcli automatically chose the cellular interface.

```
sudo nmcli connection add connection.id stream2 connection.type gsm connection.interface-name "" gsm.apn stream.co.uk gsm.username streamip gsm.password streamip
```

Expected response
```
Connection 'stream2' (1bb7a7f6-f986-4cc8-9d74-68aeb22879d9) successfully added.
```




Then read the connection profile settings

*Notes*
 * gsm.password-flags is set to 0 (none) - if this connection was added using nm-applet this would be set and hence network manager would request the user enter a password
 * I have removed some parts of the list (...) for clarity
 * connection.autoconnect : yes --- this is an example of nmcli default behaviour - because we didn't set the KVP nmcli has set autoconnect to on

 
 

```
pi@raspberrypi:~ $ nmcli connection show stream2

connection.id:                          stream2
connection.uuid:                        e2e5be6d-b64c-4b65-953d-4ff025ff6093
connection.stable-id:                   --
connection.type:                        gsm
connection.interface-name:              --
connection.autoconnect:                 yes
connection.autoconnect-priority:        0
...
gsm.number:                             *99#
gsm.username:                           streamip
gsm.password:                           <hidden>
gsm.password-flags:                     0 (none)
gsm.apn:                                stream.co.uk
gsm.network-id:                         --
gsm.pin:                                <hidden>
gsm.pin-flags:                          0 (none)
...
```


**Example 2 - add EE SIM connection with IPv4 only
At the present time IPV4V6 functionality has mixed success on UK networks. Setting to IPv4 only can fix some connectivity issues.

With the debian system installed at the time of testing ipv6.method disabled is not enabled - to workaround this we need to use ignore and then manually set the context using AT+CGDCONT
```
sudo nmcli connection add connection.id "eeno6" connection.type gsm connection.interface-name "" gsm.apn "everywhere" gsm.username "eesecure" gsm.password "secure" ipv6.method ignore 
```



### Remove connection profile "stream2"
If you carry out the following command the profile will be deleted.
Don't delete the profile if you want to use it :)
```
sudo nmcli connection delete stream2
```

### Manually start a connection using a Network Manager profile

This version specifies the interface to use - in this case cdc-wdm0 
```
sudo nmcli connection up stream2 ifname cdc-wdm0
```

This version lets network manager to choose the interface
```
sudo nmcli connection up stream2

Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/4)
```

A check to review the device interface to connection states

```
pi@raspberrypi:~ $ nmcli device status
DEVICE    TYPE      STATE         CONNECTION
eth0      ethernet  connected     Wired connection 1
cdc-wdm0  gsm       connected     stream2
wlan0     wifi      disconnected  --
lo        loopback  unmanaged     --
```

### Manually stop a connection 

```
sudo nmcli connection down stream2
```
  

### Change configuration from automatic to manually connect
Check current setting
```
pi@raspberrypi:~ $ nmcli c show 'stream2' | grep connection.autoconnect
connection.autoconnect:                 yes
connection.autoconnect-priority:        0
connection.autoconnect-retries:         -1 (default)
connection.autoconnect-slaves:          -1 (default)
```


Make the change
```
sudo nmcli c modify 'stream2' connection.autoconnect no
```

Check the result
```
pi@raspberrypi:~ $ nmcli c show 'stream2' | grep connection.autoconnect
connection.autoconnect:                 no
connection.autoconnect-priority:        0
connection.autoconnect-retries:         -1 (default)
connection.autoconnect-slaves:          -1 (default)
```

### Change PDP Context type setting

3G/4G modems support the following settings  
* IPV4
* IPV6
* IPV4V6

Comments after practical testing
* Some networks don't support IPV6
* Using the EE we have observed the HL8548 fail to IP connect when configured to use IPV4V6 - works ok when only IPV4 is enabled
* At some point in the distant future it's possible IPv4 will disappear

**PDP Context type - network manager default**
IPV4V6 is the default - profile settings are as follows 

ipv4.method:                            auto  
ipv6.method:                            auto  

**PDP Context type - set network manager to IPV4 only**
ipv4.method:                            auto    
ipv6.method:                            disabled  

To change the ipv6.method to "disabled" on a connection called "stream2" using nmcli for
 example - options at the time of writing are are [ignore, auto, dhcp, link-local, manual, shared]
```
sudo nmcli connection modify "stream2"  ipv6.method "ignore"
```
But it really should be the following - at some point debian linux will change to this
```
sudo nmcli connection modify "stream2"  ipv6.method "disabled"
```

What does this do.

```
at+cgdcont?
+CGDCONT: 1,"IP","everywhere","0.0.0.0",0,0,0,0
+CGDCONT: 2,"IPV4V6","ims","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 3,"IPV4V6","sos","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,1

OK
```



https://developer.gnome.org/NetworkManager/stable/settings-ipv6.html
https://developer.gnome.org/NetworkManager/stable/settings-ipv4.html


### Network Manager - connection profile file system locations
Configuration settings are actually stored in the file system e.g.

```
root@raspberrypi:/etc/NetworkManager# ls system-connections
```
One file for each connection profile

[For an example see](./exampleNetworkManagerConfigFile.md)  





### Network Manager - Test records 

[Testing details](./test_configurationRecords.md)



## Debug hints

### RPi syslog
```
sudo tail -f /var/log/syslog

```

### Network Manager - stop  
```
sudo /etc/init.d/network-manager stop
```

** restart network manager
After editing settings - this needs to be done

```
sudo service network-manager restart
```

even better [see](https://www.freedesktop.org/wiki/Software/ModemManager/Debugging/)

### Network Manager - restart
```
sudo service network-manager restart
```

### Have a look at running RPi processes
```
ps -U0 -o 'tty,pid,comm' | grep ^?
```


## External documentation sources
{::comment}
[Documentation on network manager](https://wiki.debian.org/NetworkManager)
{:/comment}

[Documentation on network manager](https://developer.gnome.org/NetworkManager/stable/)

[Documentation on network manager cellular command line configuration](https://docs.ubuntu.com/core/en/stacks/network/network-manager/docs/configure-cellular-connections)

[Documentation on nmcli](https://developer.gnome.org/NetworkManager/stable/nmcli.html)

[1.^] [Documentation on nmcli connection profile key value pairs](https://developer.gnome.org/NetworkManager/stable/nm-settings-nmcli.html)