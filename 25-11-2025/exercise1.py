nums=[23,89,12,78,55,42]
largest=0
second=0
for n in nums:
    if n>largest:
        second=largest
        largest=n
    elif largest>n>second:
        second=n
print("the second largest number is:",second)