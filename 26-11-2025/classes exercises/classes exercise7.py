class Customer:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def isEligible(self):
        if self.age>=25:
            return True
        else:
            return False

customer_1=Customer('Aaron',22,"Mumbai")
customer_2=Customer('Neil',26,"Mumbai")
if customer_2.isEligible():
    print("Eligible")
else:
    print("Not Eligible")



