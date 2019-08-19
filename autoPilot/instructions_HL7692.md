# HL7692 Pilot

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
Note that the LED port configuration is erased if the modem firmware is updated

The Pilot board recommended settings are as follows - the modem should be preconfigured
 like this when the Pilot board is new

#### LED D6
Set LED D6 as cellular network status indicator with the following command
```
at+ksync=2,7
```

With this setting the LED D6 behaviour is as follows

1. LED PERMANENTLY OFF: Not registered / Initialization / Registration denied / no SIM card
1. LED 600 ms ON / 600ms OFF: Not registered but searching 
1. LED 75 ms ON / 3s OFF: connected to the network

#### LED D5
Set LED D5 as the cellular Pilot module boot and power indicator  
```
at+kgpio=8,1
```

With this setting the LED D5 behaviour is as follows
1. If the modem is off then the LED will be OFF
1. Following modem powered off - if a power on signal is applied to the Pilot module 
the LED should momentarily flash on
1. Then the LED will be OFF
1. After the modem has booted the LED should be ON

### HL7692 USB port composition

Currently network manager effectively manages the HL7692 network interface 
if the HL7692 is reconfigured to USB composition 2 which gives 1 MBIM and 1 USB port.
This a change from the modules default setting 

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

## HL7692 and power on signal

Recommend using the power ON / OFF scripts to ensure correct state of modem operation - this will 
overide the RPi's GPIO default state which may not be a stable signal.

| RPi   |  HL7692 power up state  |
| --- | --- |
| RPi3B+ | Default GPIO state causes Pilot to power up  |
| RPi4   | Default GPIO state causes Pilot to be powered down |

