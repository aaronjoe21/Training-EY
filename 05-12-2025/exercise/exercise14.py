from datetime import datetime, date,time, timedelta
def check_date_status(input_date):
    if input_date>date.today():
        print("FUTURE")
    elif input_date<date.today():
        print("PAST")
    else:
        print("TODAY")

check_date_status(date(2025, 12, 5))   # Today (if run on 2025-12-05)
check_date_status(date(2025, 12, 6))   # Future
check_date_status(date(2025, 12, 1))
