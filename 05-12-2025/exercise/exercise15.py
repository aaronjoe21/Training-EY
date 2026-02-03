from datetime import datetime, date,time, timedelta
start=date(2025,3,5)
n=3
expiry=start+timedelta(days=n)
print(expiry)