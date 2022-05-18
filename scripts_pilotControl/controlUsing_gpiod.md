A replacement for wiringpi is needed as it is now obsolete. 

This example uses raspi-gpio because it's simple to use and makes (whilst the system is powered) persisent changes to GPIO output states. 

raspi-gpio is probably not suitable for commercial applications. For some alternatives see [quick review](#Quick-review-of-some-common-RPi-GPIO-tools)

# RPi controlled PiloT GPIO
| PiloT function | RPi 40W GPIO | gpiod |
| --- | --- | --- |
| POWER Supply ON | GPIO6 | gpiochip0|
| Module ON | GPIO21 | gpiochip0|
| Module RESET (don't use leave 0) | GPIO20 | gpiochip0|


# Example PiloT module power on
Power on the PiloT using the raspi-gpio command line utility.

Open a command line shell  

Power the Pilot board power on  
```
raspi-gpio set 6 op pn dh
```

PiloT module power on  
```
raspi-gpio set 21 op pn dh
```

Note from the RC76xx PTS
```
If POWER_ON_N remains connected to the GND for more than ~7s, the module will
start ok. It will turn off if POWER_ON_N is then released (OC).
```


# Example PiloT module power off
Power off the PiloT using the raspi-gpio command line utility.  

Open a command line shell  - Ideally send the power off command such as AT+CFUN=0

Signal the PiloT module to power off  
```
raspi-gpio set 21 op pn dl
```


Power the Pilot board power off   
```
raspi-gpio set 6 op pn dl
```



# Quick review of some common RPi GPIO tools
## gpioset
Partially installed in OS. Needs to be installed to access the command line tools
Lets try **[gpiod](https://github.com/brgl/libgpiod)** command line tools with Bulleye

*Install*
```
sudo apt install gpiod
```

*Summary*

It works. 

The state valid only while executing. 

IO state reverts unless you demonsize it like this
```
gpioset --mode=signal --background gpiochip0 6=1 21=0 20=0
```

The library coupled with an app that runs all the time would work but in here I'm just demo

The advantage in a real implementation is that it should work ok with other GPIO drivers

## gpiozero
gpiozero is built into OS

Python library works the same as gpiod does. When the Python script ends the GPIO is returned to initial state

Would work well for a Python based system implementation

## raspi-gpio
[raspi-gpio](https://github.com/RPi-Distro/raspi-gpio) is built into OS 

Accesses chip GPIO directly

Output states are retained even when shell is closed

Works ok for this demo

Using raspi-gpio in a product applications will be a bit of a hack as it bypasses any Linux drivers

