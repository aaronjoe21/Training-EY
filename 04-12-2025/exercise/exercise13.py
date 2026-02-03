
list1=["Henry","Doe","John","Lovam",345,45]
for i in range(0,len(list1),2):
    if type(list1[i])==str:
        list1[i]=list1[i][::-1]
    elif type(list1[i])==int:
        list1[i]=str(list1[i])[::-1]
        list1[i]=int(list1[i])

print(list1)