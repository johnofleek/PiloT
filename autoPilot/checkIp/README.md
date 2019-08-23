# Purpose
Automate testing of wwan0 network connection provided by the Pilot board by using ICMP ping
Restart the wwan0 network connection on failure
Current version is experimental - seems to work but is very basic - maybe view this
as a starting point to develop a better solution

## Quick start
```
pip install python-crontab
```

Add the cron custom job
```
cronJobAdd.py
```

After this [checkIp.py] should execute every minute


# Notes
1. consumes data due to ICMP transactions
2. targets only wwan0
3. runs even when another interface has priority

## Source
```
https://stackabuse.com/scheduling-jobs-with-python-crontab/
```

list the jobs from the command line   
```
crontab -l
```