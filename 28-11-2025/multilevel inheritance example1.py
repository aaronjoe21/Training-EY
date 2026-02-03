class Property:
    def __init__(self,place,place2):
        self.place=place
        self.place2=place2
class Building(Property):
    def __init__(self,floor,block,place,place2):
        super().__init__(place,place2)
        self.floor=floor
        self.block=block
class Apartment(Building):
    def __init__(self,flatno,type,floor,block,place,place2):
        super().__init__(floor,block,place,place2)
        self.flatno=flatno
        self.type=type
    def display(self):
        print("flatno:",self.flatno)
        print("type:",self.type)
        print("floor:",self.floor)
        print("block:",self.block)
        print("City",self.place)
        print("Country:",self.place2)


flatno=input("Enter flat number: ")
type=input("2bhk or 3bhk?: ")
floor=input("Enter floor number: ")
block=input("Which block:? (A,B,C)")
place=input("building city location:")
place2=input("building country location")

a=Apartment(flatno,type,floor,block,place,place2)
a.display()