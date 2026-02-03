class Student:
    def __init__(self, name,id, marks):
        self.name = name
        self.id = id
        self.marks = marks
    def grade(self):
        if self.marks>90:
            print("Grade is A")
        elif self.marks>80:
            print("Grade is B")
        elif self.marks>70:
            print("Grade is C")
        elif self.marks>60:
            print("Grade is D")
        else:
            print("Grade is F")
    def display(self):
        print("Name is ",self.name)
        print("ID : ",self.id)
        print("Marks is: ",self.marks)

S1=Student("Henry", 1, 95)
S2=Student("John", 2, 80)

S1.display()
S1.grade()

S2.display()
S2.grade()
