f=open("product.txt","r")
f1=open("catalog1.txt","w")
a=f.read()
b=a.split()
print(b)
f1.write("PRODUCT \t PRICE\n")
for i in range(0,len(b),2):
    f1.write(b[i])
    f1.write(b[i+1]+"\n")