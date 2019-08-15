**HL7692 Pilot**

## HL7692 module AT command configuration

### Configuration interface
With network manager or similar networking helpers disabled it is possible to manually command / configure the 
HL7692 via it's USB serial port. 

One way to access the HL7692 USB serial port is by using 
a serial terminal tool like minicom 

```
$ sudo minicom -D /dev/ttyACM0
```


### LEDs
Note that the LED port configuration is erased if the firmware is updated

HL7692 Pilot board recommended settings are 

```
at+ksync=2,7
at+kgpio=8,1
```

LED D5
Configure as a modem booted / power indicator
```  

```
### USB port composition

Currently network manager effectively manages the HL7692 network interface 
when the HL7692 is reconfigured to USB composition 2 which gives 1 MBIM and 1 USB port.  

At this time (August 2019) the Sierra AT command guide indicated that three USB serial ports 
will be made available but this wasn't the case with the available FW RHL769x.2.26 and RHL769x.2.27.

Configure the composition
```
AT+KUSBCOMP=2
```

Check the composition
```
AT+KUSBCOMP?
+KUSBCOMP: 2
```

