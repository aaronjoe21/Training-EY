list=["apple","orange","bun","pea","guava","ss"]
for i in list:
    if len(i)<3:
        list.remove(i)
print(list)