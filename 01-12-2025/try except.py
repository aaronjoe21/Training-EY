'''
try:
    print(5/0)
except ZeroDivisionError:
    print("INVALID")
'''


'''
try:
    num=int(input("Enter number:"))
    print(10/num)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
'''
'''
try:
    f=open("student.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing operarion completed")
'''
'''
try:
    value=int(int("50"))
except ValueError:
    print("Invalid conversion")
else:
    print("Conversion successful:",value)
'''

#raised function
'''
def check_age(age):
    if age<18:
        raise ValueError("Age must be 18 or above")
    return "allowed"
print(check_age(17))
'''
class LowBalanceError(Exception):
    pass
def withdraw(amount,balance):
    if amount > balance:
        raise LowBalanceError("Insufficient balance")
    return balance - amount