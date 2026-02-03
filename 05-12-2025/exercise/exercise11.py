from datetime import datetime, date,time, timedelta
start=datetime.combine(date(2025,3,5), time(10,15))
n=int(input('ENTER NO OF DAYS:'))
expiry=start+timedelta(days=n)
print(expiry)