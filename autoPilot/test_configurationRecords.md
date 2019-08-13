# Pilot board with Raspberry Pi and Raspian OS
# Record info on what was tested here

  

| What | Info |
| ---- | ---- |  
| Module | HL7692 |
| Raspberry | RPi4 |
| OS | Buster |
| OS Version (uname -a) | Linux raspberrypi 4.19.58-v7l+ #1245 SMP Fri Jul 12 17:31:45 BST 2019 armv7l GNU/Linux |
| Module Firmware | |
| Module Config |  Set to MBIM mode
| --- |   AT+KUSBCOMP=2 |  
| NetworkManager Applet Version | 1.8.20 |
| nmcli tool | version 1.14.6 |
| dpkg -s network-manager \| grep '^Version:' | Version: 1.14.6-2 |
| Notes | MBIM didn't work with earlier FW version |
|  [Y] | Working Connection |
|  [Y] | Via MBIM |  


<br/>

| What | Info |
| ---- | ---- |  
| Module | HL8548 |
| Raspberry | RPi4 |
| OS | Buster |
| OS Version (uname -a) | Linux raspberrypi 4.19.58-v7l+ #1245 SMP Fri Jul 12 17:31:45 BST 2019 armv7l GNU/Linux |
| Module Firmware | |
| Module Config |  Set to CDC-ECM mode
| --- |   AT+KUSBCOMP=2 | 
| nmcli tool | version 1.14.6 |
| NetworkManager Applet Version | 1.8.20 |
| dpkg -s network-manager \| grep '^Version:' | Version: 1.14.6-2 |
| Notes | Network manager doesn't try to connect the CDC-ECM port |
| Notes | Network manager will connect using PPP over CDC-ACM4 | 
| Notes | dhcpcd does still manage CDC_ECM when AT+XCEDATA=2,0 is used |
|  [Y] | Working Connection |
|  [N] | Via MBIM |
  

<br/>


| What | Info |
| ---- | ---- |  
| Module | EM7455 |
| Raspberry | RPi4 |
| OS | Buster |
| OS Version (uname -a) | Linux raspberrypi 4.19.58-v7l+ #1245 SMP Fri Jul 12 17:31:45 BST 2019 armv7l GNU/Linux |
| Module Firmware | SWI9X30C_02.24.05.06 r7040 CARMD-EV-FRMWR2 2017/05/19 0 |
| Module Config |  Set to MBIM mode |
| --- |  at!usbcomp? 
| --- | Config Index: 1                                                                 
| --- | Config Type:  1 (Generic)                                                       
| --- | Interface bitmask: 0000100D (diag,nmea,modem,mbim)   |  
| NetworkManager Applet Version | 1.8.20 |
| nmcli tool | version 1.14.6 |
| dpkg -s network-manager \| grep '^Version:' | Version: 1.14.6-2 |
| Notes | Network manager unable to set up a connection an attempt is made
|  [N] | Working Connection |
|  [N] | Via MBIM |


<br/>



| What | Info |
| ---- | ---- |  
| Module | EM7455 |
| Raspberry | RPi4 |
| OS | Buster |
| OS Version (uname -a) | Linux raspberrypi 4.19.58-v7l+ #1245 SMP Fri Jul 12 17:31:45 BST 2019 armv7l GNU/Linux |
| Module Firmware | Revision: SWI9X30C_02.32.11.00 r8042 CARMD-EV-FRMWR2 2019/05/15 21:52:20 |
| Module Config |  Set to MBIM mode |
| --- |  at!usbcomp? 
| --- | Config Index: 1                                                                 
| --- | Config Type:  1 (Generic)                                                       
| --- | Interface bitmask: 0000100D (diag,nmea,modem,mbim)   |  
| NetworkManager Applet Version | 1.8.20 |
| nmcli tool | version 1.14.6 |
| dpkg -s network-manager \| grep '^Version:' | Version: 1.14.6-2 |
| Notes | Network manager made connection first time using MBIM cdc-wdm0
| Notes | Speed test ~20Mbps down 13Mbps/29Mbps up at+cops? +cops: 0,0,"3",7 |
|  [Y] | Working Connection |
|  [Y] | Via MBIM |
|  [Y] | [some speed testing](./speedtests/Rpi4EM7455_uPilot_USB3_threeNetwork_2019-08-13-111021_1920x1200_scrot.png)  |
<br/>