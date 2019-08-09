#!/bin/sh

#
#   Power signal to HL module
#   OFF
#   Depends on gpio being installed http://wiringpi.com/the-gpio-utility/

gpio -g mode 6 out
gpio -g write 6 0
gpio -g mode 21 out
gpio -g write 21 0
