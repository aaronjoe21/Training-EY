numbers=(33,20,30,60,50)
maximum=0
minimum=numbers[0]
for i in range(0,len(numbers)):
    if numbers[i]>maximum:
        maximum=numbers[i]
for i in range(0,len(numbers)):
    if numbers[i]<minimum:
        minimum=numbers[i]
print("max=",maximum)
print("min=",minimum)
