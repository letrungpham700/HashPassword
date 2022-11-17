import datetime

def Today():
    day_scan = datetime.date.today().strftime('%Y-%m-%d')
    return day_scan

def TimeYesterday():
    #Check date today
    check_today = datetime.date.today()
    #Check date yesterday
    check_yesterday = check_today - datetime.timedelta(days=1)
    #Format date yesterday to string
    yesterday = check_yesterday.strftime('%Y-%m-%d')
    return yesterday
