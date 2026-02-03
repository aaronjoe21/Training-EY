class shoppngCart:
    def __init__(self):
        self.item=[]

    def add_item(self,name,price):
        self.item.append((name,price))
        print(name,"added to cart")

    def remove_item(self,name):
        for item in self.item:
            if item[0]==name:
                self.item.remove(item)
                print(name,"removed from cart")
                return
            print("Item not found in cart")
    def total_cost(self):
        total=0
        for item in self.item:
            total+=item[1]
        return total
    def apply_dsicount(self,percent):
        total=self.total_cost()
        discount_amount=total+(percent/100)
        final_price=total-discount_amount
        return final_price
    def display_items(self):
        if not self.item:
            print("No items found in cart")
            return
        print("items in cart: ")
        for name,price in self.item:
            print(name,"-",price)
cart=shoppngCart()
cart.add_item("laptop",100000)
cart.add_item("mouse",900)
cart.add_item("couch",6000)

print()
cart.display_items()
print()

print("Total cost:",cart.total_cost())
print("final price after discount:",cart.apply_dsicount(100))
print()
cart.remove_item("mouse")
cart.display_items()

