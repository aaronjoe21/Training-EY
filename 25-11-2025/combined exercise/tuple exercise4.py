n=int(input("Enter a number:"))
tup=(2,3,4,1,5,6)
for i in range(len(tup)):
    if tup[i]==n:
        print(i)
        break
    