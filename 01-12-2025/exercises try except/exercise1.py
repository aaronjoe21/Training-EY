n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
try:
    print("Division:",n1/n2)
except ZeroDivisionError:
    print("Division Error")