from datetime import datetime, date,time, timedelta

sample = [
    datetime(2025, 3, 3, 9, 0),   # Monday
    datetime(2025, 3, 4, 9, 0),   # Tuesday
    datetime(2025, 3, 10, 9, 0),  # Monday
]
count=0
for i in sample:
    if i.weekday()==0:
        count+=1
print("Number of Mondays=",count)
