from datetime import datetime,date,timedelta
date_of_birth=input("Enter the date of birth in YYYY-MM-DD format:")

D_O_B=datetime.strptime(date_of_birth,"%Y-%m-%d").date()
print(D_O_B)
today=date.today()
precise_age=today-D_O_B
days = precise_age.days
years = days // 365  # approximate
months = (days % 365) // 30
remaining_days = (days % 365) % 30

print(f"Age: {years} years, {months} months, {remaining_days} days")
