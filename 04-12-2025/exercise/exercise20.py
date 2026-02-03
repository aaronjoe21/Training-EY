class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

# Test
a1 = BankAccount(5000)
a2 = BankAccount(3000)
print("Total Balance:", a1 + a2)
