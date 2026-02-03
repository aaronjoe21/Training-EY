bill_amount = int(input("Enter your billing amount: "))
bank_balance = int(input("Enter your bank balance: "))
option = int(input("Enter your option: Google Pay-1, PhonePay-2, PayTM-3 "))


class Payment:
    def pay(self, message):
        print("Processing payment:", message)


class GooglePay(Payment):
    def pay(self, message):  # Overriding
        print("Payment done via Google Pay:", message)


class PhonePay(Payment):
    def pay(self, message):  # Overriding
        print("Payment done via Phone Pay:", message)


class PayTM(Payment):
    def pay(self, message):  # Overriding
        print("Payment done via PayTM:", message)


# Usage
if bill_amount <= bank_balance:
    order_details = input("Enter your order details: ")
    payment_id = int(input("Enter your Payment Id: "))
    message = f"Order: {order_details}, Payment ID: {payment_id}"

    if option == 1:
        payment = GooglePay()
    elif option == 2:
        payment = PhonePay()
    else:
        payment = PayTM()

    payment.pay(message)  # Polymorphism in action
else:
    print("Insufficient balance! Payment cannot be processed.")