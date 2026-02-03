num=['a','b','c','d','e']
a=num[0]
num[0]=num[len(num)-1]
num[len(num)-1]=a
print("reversed",num)