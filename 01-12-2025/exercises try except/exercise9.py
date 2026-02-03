n1=input("Enter a number")
n2=input("Enter another number")
try:
    n1=float(n1)
    n2=float(n2)
except ValueError:
    print("only numbers are allowed")
else:
    try:
        print("add=",n1+n2)
        print("sub=",n1-n2)
        print("mul=",n1*n2)
        print("div=",n1/n2)
    except ZeroDivisionError:
        print("division by zero")
    except:
        print("something went wrong")