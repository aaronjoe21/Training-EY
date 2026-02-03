class Company():
    def __init__(self,id,department):
        self.id=id
        self.department=department
class Employee(Company):
    def __init__(self,name,id,department):
        super().__init__(id,department)
        self.name=name
    def display(self):
        print("Employee id:", self.id)
        print("Employee name:", self.name)
        print("Department:", self.department)

id=int(input("Enter employee ID:"))
department=input("Enter department:")
name=input("Enter employee name:")
a=Employee(name,id,department)
a.display()