from pyexpat import model


class Product():
    def __init__(self,price, manufacturer,productid):
        self.price=price
        self.manufacturer=manufacturer
        self.productid=productid
class electronicProduct(Product):
    def __init__(self,name,model,price,productid,manufacturer):
        super().__init__(price,manufacturer,productid)
        self.name=name
        self.model=model
    def display(self):
        print(self.name,self.model,self.price,self.manufacturer)
name=input("electronic product:")
model=input("model")
price=input("price")
productid=input("product id")
manufacturer=input("manufacturer")
a=electronicProduct(name,model,price,productid,manufacturer)
a.display()