---
layout: default
title: Automation - IP link check
parent: Pilot

nav_order: 10
has_children: false
---


## Purpose
Automates IP link availablity - reboots the PiloT if the IP link fails.
By testing wwan0 network connection provided by the Pilot board using ICMP ping  
Restarts the wwan0 network connection on ping failure   
The current version is experimental - seems to work but is very basic - maybe view this  
as a starting point to develop a better solution  

## Quick start
```
pip install python-crontab
```

This assumes the Pilot project was installed in the pi@raspberrypi: home folder - the code 
currently has hardcoded paths  

Add the cron custom job  
```
python cronJobAdd.py
```


After this [checkIp.py] should execute every minute


# Notes
1. consumes data due to ICMP transactions
2. targets only wwan0
3. runs even when another interface has priority
4. hardcode paths
5. sends ping via wwan0 every minute
6. hardcoded ping server address
7. hardcoded tested interface 
1. hardcoded ping rate

## Source
```
https://stackabuse.com/scheduling-jobs-with-python-crontab/
```

## Further stuff

list all the jobs from the command line   
```
crontab -l
```

Remove all cron jobs
```
python cronJobRemove.py
```
