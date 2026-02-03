class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def add(self):
        print("name:", self.name)
        print("price:", self.price)
        print("quantity:", self.quantity)
        total=self.price*self.quantity
        print("total=",total)


p1=Product("Chocolates",10, 50)
p2=Product("Bananas",20, 50)
p3=Product("Mangas",23, 60)

p1.add()
p2.add()
p3.add()