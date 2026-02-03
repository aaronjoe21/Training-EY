#
# class Student:
#     pass
#
# s1=Student()
# s2=Student()
#
#
# class Student:
#     def __init__(self,name,age):#constructor #self is the object of the current class
#         self.name=name
#         self.age=age
#
# s3=Student("Abdullah",35)
# s4=Student("Rahul",28)
# print(s3.name,s3.age)
# print(s4.name,s4.age)


# class car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def display(self):
#         print("Brand:",self.brand)
#         print("Model:",self.model)
#         print("Price:",self.price)
#
# car1=car("Toyota","fortuner",450000)
# car2=car("Hyundai","Creta",500000)
# car3=car("tesla","model 3",600000)
#
# car1.display()
# print()
# car2.display()
# print()
# car3.display()
#
# class Employee:
#     def __init__(self,emp_id,name,department,salary):
#         self.emp_id=emp_id
#         self.name=name
#         self.department=department
#         self.salary=salary
#     def display(self):
#         print("Employee ID:",self.emp_id)
#         print("Name:",self.name)
#         print("Department:",self.department)
#         print("Salary:",self.salary)
# e1=Employee(101,"Abdullah","IT",95000)
# e2=Employee(102,"Rahul","Finance",75000)
#
# e1.display()
# print()
# e2.display()

#
# class BankAccount:
#     def __init__(self, Customer_Name, Account_Number, Balance):
#         self.Customer_Name = Customer_Name
#         self.Account_Number = Account_Number
#         self.Balance = Balance
#     def display(self):
#         print("Customer Name:", self.Customer_Name)
#         print("Account Number:", self.Account_Number)
#         print("Balance:", self.Balance)
#     def deposit(self, amount):
#         self.Balance += amount
#     def withdraw(self, amount):
#         self.Balance -= amount
# # creating objects
# a1 = BankAccount("Mavrick", 100120033456, 50000)
# # depositing money
# a1.deposit(int(input("Enter amount to deposit:")))
# a1.display()
# print()
# # withdrawing money
# a1.withdraw(int(input("Enter amount to withdraw:")))
# a1.display()




