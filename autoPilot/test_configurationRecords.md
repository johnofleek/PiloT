# Pilot on Raspberry Pi and raspian
# Keep info on what was tested here

  

|  What | Info |
| ---- | ---- |  
| Module | HL7692 |
| Raspberry | RPi4 |
| OS | Buster |
| OS Version (uname -a) | Linux raspberrypi 4.19.58-v7l+ #1245 SMP Fri Jul 12 17:31:45 BST 2019 armv7l GNU/Linux |
| Module Config |  Set to MBIM mode
| --- |   AT+KUSBCOMP=2 |  


<br/>

|  What | Info |
| ---- | ---- |  
| Module | HL8548 |
| Raspberry | RPi4 |
| OS | Buster |
| OS Version (uname -a) | Linux raspberrypi 4.19.58-v7l+ #1245 SMP Fri Jul 12 17:31:45 BST 2019 armv7l GNU/Linux |
| Module Config |  Set to CDC-ECM mode
| --- |   AT+KUSBCOMP=2 | 
| Notes | Network manager doesn't try to connect the CDC-ECM port |
| Notes | Network manager will connect using PPP over CDC-ACM4 | 
| Notes | dhcpcd does still manage CDC_ECM when AT+XCEDATA=2,0 is used |



<br/>