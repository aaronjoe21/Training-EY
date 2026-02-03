old= ("python", "cloud", "data")
new=[]
for i in old:
    n=i[::-1]
    new.append(n)
new=tuple(new)
print(new)