a= {"a": 1, "b": 2}
b= {"b": 3, "c": 4 }
inverted={}
for key,value in a.items():
    if key in inverted:
        inverted[key].append(value)
    else:
        inverted[key]=[value]
for key,value in b.items():
    if key in inverted:
        inverted[key].append(value)
    else:
        inverted[key]=[value]
print(inverted)