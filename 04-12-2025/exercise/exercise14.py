dict1={
    "Henry":47500,
    "Bance":29800,
    "John":650000,
    "Mary":60001,
}
dict2={}
for key,value in dict1.items():
    if value>60000:
        dict2.update({key:value})

print(dict2)