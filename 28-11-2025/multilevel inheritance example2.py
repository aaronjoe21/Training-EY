class device:
    def __init__(self,Brand,model,price):
        self.Brand=Brand
        self.model=model
        self.price=price
class computer(device):
    def __init__(self,Brand,model,price,processor,ram):
        super().__init__(Brand,model,price)
        self.processor=processor
        self.ram=ram
class laptop(computer):
    def __init__(self,Brand,model,price,processor,ram,Battery,weight):
        super().__init__(Brand,model,price,processor,ram)
        self.Battery=Battery
        self.weight=weight
    def display(self):
        print(self.Brand)
        print(self.model)
        print(self.price)
        print(self.processor)
        print(self.ram)
        print(self.Battery)
        print(self.weight)


Brand=input("brand")
model=input("model")
price=input("price")
Processor=input("processor")
ram=input("ram")
Battery=input("battery")
weight=input("weight")
a=laptop(Brand,model,price,Processor,ram,Battery,weight)
a.display()