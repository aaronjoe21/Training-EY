f=open("report.txt","w")
b=("""
    _________________________________________            
                REPORT
    -----------------------------------------
    """)
f.write(b)
f.close()

def write_report_record(name,price):
    record=f"""
    * {name} - {price}
    ----------------------------------------------
    """
    with open("report.txt","a") as c:
        c.write(record)



sum1=0
while True:
    n=input("DO YOU WANT TO ADD EXPENSE: (YES/NO) or DISPLAY")
    if n=="YES":
        name=input("Enter expense name:")
        price=int(input("Enter expense price:"))
        sum1+=price
        write_report_record(name,price)
    elif n=="NO":
        d=open("report.txt","a+")
        d.write(f"TOTAL EXPENSE:{sum1}")
        d.seek(0)
        print(d.read())
        d.close()
        break


