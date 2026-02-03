class Product:
    def __init__(self,name,price,warranty):
        self.name = name
        self.price = price
        self.warranty = warranty
    def electronics(self):
        self.warranty = int(self.warranty)+int(input("Enter Additional Warranty:"))
        print("Total warranty",self.warranty)
    def display(self):
        print("Name",self.name)
        print("Price",self.price)
        print("No.of warranty years",self.warranty)
P1=Product("P1","30000","5")

P1.display()
P1.electronics()