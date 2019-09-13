from crontab import CronTab

cron = CronTab(user=True)

for job in cron:
    print(job)

x = cron.remove_all()

print x

print "done remove"

cron.write() ## needs the write or it won't get changed