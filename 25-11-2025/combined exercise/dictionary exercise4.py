a={"apple":10,"banana":200,"orange":101,"peas":99}
b={}
for key,value in a.items():
    if a[key]>100:
        b[key]=value
print(b)