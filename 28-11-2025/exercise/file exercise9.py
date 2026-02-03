f=open("exercise9.txt","w")
for i in range(11):
    s=i**2
    b=str(s)
    f.write(b)
    f.write("\n")