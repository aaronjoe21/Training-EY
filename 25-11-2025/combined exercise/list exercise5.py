old= [[1, 2], [3, 4], [5]]
new=[]
for i in old:
    for j in range(len(i)):
        new.append(i[j])
print(new)