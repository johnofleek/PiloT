# modem manager notes

The following are notes on an evaluation of using the Raspberry Pi + WASP2 + HL7802 module with modem manager. They are also a helpful example on how to debug issues with modem manager.

At the moment the investigation is stalled due to  
https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/issues/305

## modem manager versions
Buster version as shipped with Raspian (as of 2020/12)
```
mmcli --version
mmcli 1.10.0
```

As part of the investigation I installed a later version  
http://marksrpicluster.blogspot.com/2019/12/add-buster-backports-to-raspberry-pi.html  
this didn't fix the issue

```
sudo apt -t buster-backports install modemmanager
mmcli --version
mmcli 1.14.8
```

## HL7802 physical connection

For testing purposes the HL7802 physical UART was connected to a USB to TTY serial port board. This resulted in the UART appearing to the RPi as 

```/dev/ttyUSB0```

In order for modem manager to "probe" ttyUSB0 we need to add a udev rule.

Add this text in file /etc/udev/rules.d/ttyACM1-HL7702.rules

```
ACTION=="add|change|move", KERNEL=="ttyUSB0", ENV{ID_MM_TTY_FLOW_CONTROL}="none", ENV{ID_MM_TTY_BAUDRATE}="115200", ENV{ID_MM_CANDIDATE}="1", ENV{ID_MM_DEVICE_PROCESS}="1",ENV{ID_MM_PORT_TYPE_AT_PPP}="1"
```

For documentation see 

see https://man7.org/linux/man-pages/man8/udevadm.8.html

Then to test 
```
sudo udevadm control --reload-rules

sudo udevadm test -a -p  $(udevadm info -q path -n /dev/ttyUSB0)
```

## Debug modem manager

Enable modem manager debug to syslog
```
sudo mmcli --set-logging=DEBUG
Successfully set logging level
```

Observe the debug output
```
tail -f /var/log/syslog
```

Example connection test
```
mmcli -m 0 --simple-connect="apn=internet,username=eesecure,password=secure"
```

## stop modem manager
helps with minicom

sudo systemctl stop ModemManager



## HL7802 modem manager bug investigation - WIP 

nmcli debug
```
sudo nmcli connection up ee ifname ttyUSB0
```

Running registration checks (CS: 'no', PS: 'no', EPS: 'yes')

Jan 11 16:38:32 raspberrypi ModemManager[385]: <debug> (ttyUSB0): --> 'AT+CEREG?<CR>'
Jan 11 16:38:32 raspberrypi ModemManager[385]: <debug> (ttyUSB0): <-- '<CR><LF>+CEREG: 2'
Jan 11 16:38:32 raspberrypi ModemManager[385]: <debug> (ttyUSB0): <-- ',0<CR><LF><CR><LF>OK<CR><LF>'
Jan 11 16:38:32 raspberrypi ModemManager[385]: <debug> Modem not yet registered in a 3GPP network... will recheck soon

Running registration checks (CS: 'no', PS: 'no', EPS: 'yes')


Do it looks like when jammed in GSM the modem oks creg but not cereg

```
+CEREG: 2,0

+CREG: 0,1

```


From https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html

https://www.freedesktop.org/software/ModemManager/api/latest/ModemManager-Common-udev-tags.html#ID-MM-PORT-TYPE-AT-PPP:CAPS


```
mmcli -m 0 --output-keyvalue

...
modem.generic.supported-modes.length            : 1
modem.generic.supported-modes.value[1]          : allowed: 2g, 4g; preferred: none
modem.generic.current-modes                     : allowed: 2g, 4g; preferred: none
...
```

Ok but we jammed the modem into 2G

Maybe try
```
sudo mmcli -m 0 --set-allowed-modes "2G|4G"
error: couldn't set current
modes: 'GDBus.Error:org.freedesktop.ModemManager1.Error.Core.Unsupported: Setting allowed modes not supported'
```



