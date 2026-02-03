class mobile:
    def __init__(self,Brand,model,storage):
        self.Brand=Brand
        self.model=model
        self.storage=storage
    def upgrade(self):
        self.storage=self.storage*2
    def display(self):
        print(self.Brand)
        print(self.model)
        print(self.storage)

m=mobile("Samsung","G3",128)
while True:
    user=input("Do you want to upgrade your storage:")
    if user=="Yes":
        m.upgrade()
        m.display()
    elif user=="No":
        print("Alright")
        break
    else:
        break

