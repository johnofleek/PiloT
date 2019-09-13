#!/bin/env python2

# add cron job to cron

from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='python /home/pi/Pilot/autoPilot/checkIp/checkIp.py')
job.minute.every(1)
job.enable()

cron.write()