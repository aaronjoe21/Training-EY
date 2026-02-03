n=int(input("Enter how many numbers:"))
first=0
second=0
for i in range(n):
    n1=int(input("Enter a number:"))
    if n1 > first:
        second=first
        first=n1
    elif n1<first and n1>second:
        second=n1
print("second:",second)
