from datetime import datetime, date,time, timedelta
count=0
n=date(2024,1,1)
end=date(2024,12,31)
while n<=end:
    l=["Monday","Tuesday","Wednesday","Thursday","Friday"]
    if n.strftime("%A") in l:
        count+=1
    n= n + timedelta(days=1)
print("Number of week days=",count)