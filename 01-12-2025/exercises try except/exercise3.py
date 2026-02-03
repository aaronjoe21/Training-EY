def conversion(n):
    try:
        a=int(n)
        print(a)
    except ValueError:
        print("Value Error")



n=input("Enter a number:")
conversion(n)