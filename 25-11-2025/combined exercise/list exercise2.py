list=[1,2,3,2,4,1,5,1]
new=[]
for i in range(len(list)):
    if list[i] in new:
        continue
    else:
        count=0
        for j in range(len(list)):
            if list[i]==list[j]:
                count+=1
        if count>1:
            new.append(list[i])
print(new)


