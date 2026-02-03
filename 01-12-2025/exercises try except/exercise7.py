list=[1,3.2,"strong","2.3"]
converted=[]

for i in list:
    try:
        a=float(i)
        a=int(a)
        converted.append(a)
    except ValueError:
        print("Invalid input")
print(converted)

