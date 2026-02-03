class LowBalanceError(Exception):
    """Raised when balance is insufficient for withdrawal."""
    pass
def withdrawal(n,balance):
    if n > balance:
        raise LowBalanceError(f"Insufficient balance: balance={balance}, attempted={n}")
    else:
        balance=balance-n
        print(f"Successfully withdrawn {n}, BALANCE={balance}")


balance=10000
n=int(input("Enter the amount you want to withdrawal: "))
withdrawal(n,balance)