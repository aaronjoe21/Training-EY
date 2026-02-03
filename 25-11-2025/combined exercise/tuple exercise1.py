tup=('a',1,2,3,'b','g',3,'e')
tup1=[]
tup2=[]
for i in range(len(tup)):
    if type(tup[i])==int:
        tup1.append(tup[i])
    else:
        tup2.append(tup[i])
print("integer tuple:",tuple(tup1))
print("string tuple2:",tuple(tup2))
