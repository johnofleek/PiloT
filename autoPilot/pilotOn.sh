#!/bin/sh

#
#   Power signal to HL module
#   ON
#   Depends on gpio being installed http://wiringpi.com/the-gpio-utility/

gpio -g mode 6 out
gpio -g write 6 1
gpio -g mode 21 out
gpio -g write 21 1
gpio -g write 21 0
