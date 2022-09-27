import secrets
import schedule
import time


def importanttask():
    print('gettinh money')
    
schedule.every(10).seconds.do(importanttask)
schedule.every().monday.do(importanttask)
schedule.every().monday.at("08:00").do(importanttask)
schedule.every().day.at("08:00").do(importanttask)

while 1:
    schedule.run_pending()
    time.sleep(1)