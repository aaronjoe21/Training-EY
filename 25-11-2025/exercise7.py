num=[10,3,5,12,8,7,1]
even=[]
odd=[]
for i in range(0,len(num)):
    if num[i]%2==0:
        even.append(num[i])
    else:
        odd.append(num[i])
print("even",even)
print("odd",odd)