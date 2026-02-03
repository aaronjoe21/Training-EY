class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def total(self):
        return self.m1 + self.m2 + self.m3

    def percentage(self):
        return (self.total() / 300) * 100

    def grade(self):
        if self.percentage() > 90:
            return "A"
        elif self.percentage() < 80:
            return "B"
        elif self.percentage() < 70:
            return "C"
        elif self.percentage() < 60:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student name:", self.name)
        print("Marks: ", self.m1, self.m2, self.m3)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


# Creating an object
s1 = Student("Alex", 10, 20, 30)
s1.display()