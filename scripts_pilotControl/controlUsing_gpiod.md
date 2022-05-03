A replacement for wiring pi is needed as it is now obsolete.

Lets try **[gpiod](https://github.com/brgl/libgpiod)** with Bulleye

gpioset --mode=signal --background gpiochip1 23=1 24=0


# RPi controlled PiloT GPIO
| PiloT function | RPi 40W GPIO | gpiod |
| --- | --- | --- |
| POWER Supply ON | GPIO6 | gpiochip0  "GPIO6"|


# Install
```
sudo apt install gpiod
```
