def leap_year(year):
    if year % 4==0 and year % 100!=0 or year % 400==0:
        return True
    else:
        return False

year1=int(input("Enter the year to check the leap year: "))
leap_year=leap_year(year1)
print(leap_year)
