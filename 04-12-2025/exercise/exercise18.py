# Amazon Payment Class

bill_amount = int(input("Enter your billing amount: "))
bank_balance = int(input("Enter your bank balance: "))
option = int(input("Enter your option: Credit Card-1, UPI-2"))

class Payment:
    def pay(self, message):
        print("Processing payment:", message)

class Credit_card(Payment):
    def pay(self, message):  # Overriding
        print("Payment done via Credit Card:", message)

class UPI(Payment):
    def pay(self, message):  # Overriding
        print("Payment done via UPI:", message)

# Usage
if bill_amount <= bank_balance:
    order_details = input("Enter your order details: ")
    payment_id = int(input("Enter your Payment Id: "))
    message = f"Order: {order_details}, Payment ID: {payment_id}"

    if option == 1:
        payment = Credit_card()
        payment.pay(message)
    elif option == 2:
        payment = UPI()
        payment.pay(message)  # Polymorphism in action
    else:
        print("Insufficient balance! Payment cannot be processed.")
