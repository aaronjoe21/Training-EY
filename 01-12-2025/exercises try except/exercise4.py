def access(list,n):
    try:
        print(list[n])
    except IndexError:
        print("Index Error")
list=[0,1,5,4,3,6,7]
n=int(input("enter the index"))
access(list,n)