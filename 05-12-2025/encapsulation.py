class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Invalid depost amount")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Invalid depost amount")
    def get_balance(self):
        return self.__balance
acc=BankAccount("Shireen",5000)
acc.deposit(2000)
print(acc.get_balance())

acc.withdraw(3000)
print(acc.get_balance())

acc.__balance=100000
print(acc.get_balance())
print(dir(acc))