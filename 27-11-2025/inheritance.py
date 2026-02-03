

class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):  #dog gets animal properties because we calledanimal in dog
    def bark(self):
        print("Dog makes a bark")
d=Dog()
d.speak() #inherited


'''
class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name) #super is used to call parent constructor 
        self.emp_id=emp_id
e=Employee("Aaron", 25)
print(e.name,e.emp_id)
'''

