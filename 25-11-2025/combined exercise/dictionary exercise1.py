dict= {"A": 85, "B": 92, "C": 78, "D": 92}
max=0
for i in dict.values():
    if max<i:
        max=i
for k in dict:
    if dict[k]==max:
        print(k)
