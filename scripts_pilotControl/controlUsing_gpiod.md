A replacement for wiring pi is needed as it is now obsolete.

Lets try **[gpiod](https://github.com/brgl/libgpiod)** with Bulleye




# RPi controlled PiloT GPIO
| PiloT function | RPi 40W GPIO | gpiod |
| --- | --- | --- |
| POWER Supply ON | GPIO6 | gpiochip0|
| Module ON | GPIO21 | gpiochip0|
| Module RESET (don't use leave 0) | GPIO20 | gpiochip0|


# Install
```
sudo apt install gpiod
```

# Try some commands

Power on
```
gpioset --mode=signal --background gpiochip0 6=1 21=0 20=0
```

Power ON and module ON - module RESET OFF
```
gpioset --mode=signal --background gpiochip0 6=1 21=1 20=0
```
