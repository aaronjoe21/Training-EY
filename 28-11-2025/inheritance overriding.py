
class emailnotification(notification):
    def send(self,message):
        print("Sending email:", message)
class smsnotification(notification):
    def send(self,message):
        print("sending sms",message)
class pushnotification(notification):
    def send(self,message):
        print("Sending push:", message)

n1=emailnotification()
n1.send("your order is confirmed")

n2=smsnotification()
n2.send("your otp is confirmed")

n3=pushnotification()
n3.send("you have new message")