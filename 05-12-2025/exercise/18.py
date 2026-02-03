from datetime import date, timedelta

products=[["Bread",date(2025,12,30)],["Sweet",date(2025,12,6)]]
i=1
today_date=date.today()
for product in products:
    if product[i]-today_date< timedelta(days=15):
        print(f"{product[0]} will expire within the next 15 days")
    else:
        print(f"{product[0]} will expire after 15 days")

