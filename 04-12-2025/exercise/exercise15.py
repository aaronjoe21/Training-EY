dict1 = {
    "Henry":3000,
    "John":4000,

}
dict2 = {
    "Henry":3500,
    "John": 2000
}
for key,value in dict1.items():
    if key in dict2:
        dict2[key]+=value


print(dict2)
