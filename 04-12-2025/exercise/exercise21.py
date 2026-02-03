
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item, price):
        self.items.append((item, price))

    def remove(self, item):
        self.items = [i for i in self.items if i[0] != item]

    def total(self):
        return sum(price for _, price in self.items)

    def apply_discount(self, percent):
        return self.total() * (1 - percent/100)

# Test
cart = ShoppingCart()
cart.add("Book", 200)
cart.add("Pen", 50)
print("Total:", cart.total())
print("After Discount:", cart.apply_discount(10))
