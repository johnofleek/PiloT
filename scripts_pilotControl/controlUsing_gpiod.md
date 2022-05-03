A replacement for wiringpi is needed as it is now obsolete. This example uses gpiozero because it's simple but probably not suitable for a commercial application see [quick review](#Quick-review-of-some-common-RPi-GPIO-tools)





# Quick review of some common RPi GPIO tools
## gpioset
Partially installed in OS. Needs to be installed to access the command line tools
Lets try **[gpiod](https://github.com/brgl/libgpiod)** command line tools with Bulleye

*Install*
```
sudo apt install gpiod
```

*Summary*
It works
The state valid only while executing. IO state reverts unless you demonsize it like this
```
gpioset --mode=signal --background gpiochip0 6=1 21=0 20=0
```


The library coupled with an app that runs all the time would work but in here I'm just demoin
Advantage in a real implementation is that it should work ok with othr GPIO drivers

## gpiozero
[gpiozero](https://github.com/RPi-Distro/raspi-gpio) is built into OS

Python library works the same as gpiod does. When the Python script ends the GPIO is returned to initial state

## raspi-gpio
[raspi-gpio](https://github.com/RPi-Distro/raspi-gpio) is built into OS
Accesses chip GPIO directly
Output states are retained 
Works ok for this demo
It is a bit of a hack for production use


## RPi controlled PiloT GPIO
| PiloT function | RPi 40W GPIO | gpiod |
| --- | --- | --- |
| POWER Supply ON | GPIO6 | gpiochip0|
| Module ON | GPIO21 | gpiochip0|
| Module RESET (don't use leave 0) | GPIO20 | gpiochip0|







