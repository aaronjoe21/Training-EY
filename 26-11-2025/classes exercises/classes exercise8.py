class BankAccount:
    def __init__(self,account_number,Name,balance):
        self.account_number=account_number
        self.Name=Name
        self.balance=balance
        self.transactions=[]
    def deposit(self,amount):
        self.balance=self.balance+amount
        self.transactions.append(f"Deposit: {amount},balance:{self.balance}")
    def withdraw(self,amount):
        self.balance=self.balance-amount
        self.transactions.append(f"Withdraw:{amount},balance:{self.balance}")
    def balances(self):
        print(self.balance)
    def logs(self):
        print(self.transactions)

n=0

A1=BankAccount(101,"Aaron",50000)
while True:
    n = input("What do you want to do? (deposit, withdraw, balance check, transcations logs")
    if n=="deposit":

        amount = int(input("Enter amount:"))
        A1.deposit(amount)
    elif n=="withdraw":
        amount = int(input("Enter amount:"))
        A1.withdraw(amount)
    elif n=="balance":
        A1.balances()
    elif n=="transcations":
        A1.logs()
    elif n=="exit":
        break
    else:
        print("Invalid input")