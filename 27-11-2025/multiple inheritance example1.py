class phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display1(self):
        print("PHONE DETAILS")
        print("brand:",self.brand)
        print("model:",self.model)
        print("price:",self.price)
class camera:
    def __init__(self,pixel):
        self.pixel=pixel

    def display2(self):
        print("PIXEL:",self.pixel)
        print("Photo clicked")
class smartphone(phone,camera):
    def __init__(self,brand,model,price,pixel,simtype,battery):
        phone.__init__(self,brand,model,price)
        camera.__init__(self,pixel)
        self.simtype=simtype
        self.battery=battery
    def display(self):
        print("Smartphone details")
        print("brand:",self.brand)
        print("model:",self.model)

brand=input("enter brand")
model=input("enter model")
price=input("enter price")
pixel=input("enter pixel")
simtype=input("enter simtype")
battery=input("enter battery")
a=smartphone(brand,model,price,pixel,simtype,battery)
while True:
    n=input("DO YOU WANT DETAILS OF PHONE OR SMARTPHONE OR CLICK A PHOTO( PHONE, SMARTPHONE,CLICK)")
    if n=="phone":
        a.display1()
    elif n=="smartphone":
        a.display()
    elif n=="click":
        a.display2()
    elif n=="exit":
        break
