num=[0,3,0,5,7,0,9]
zeros=[]
nonzero=[]
for i in range(0,len(num)):
    if num[i]==0:
        zeros.append(num[i])
    elif num[i]!=0:
        nonzero.append(num[i])
nonzero.extend(zeros)
print(nonzero)