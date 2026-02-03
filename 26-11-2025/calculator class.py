class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def display(self):
        print("num1:",self.num1)
        print("num2:",self.num2)
    def add(self):
        self.num=self.num1+self.num2
        print(num1,"+",num2,"=",self.num)
    def sub(self):
        self.num=self.num1-self.num2
        print(num1,"-",num2,"=",self.num)
    def mul(self):
        self.num=self.num1*self.num2
        print(num1,"*",num2,"=",self.num)
    def div(self):
        if num2==0:
            print(num1,"/",num2,"= division by zero Error")
        else:
            self.num=self.num1/self.num2
            print(num1,"/",num2,"=",self.num)


num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
a=calculator(num1,num2)
a.display()
operations=input("enter operations:")
if operations=="add":
    a.add()
elif operations=="sub":
    a.sub()
elif operations=="mul":
    a.mul()
else:
    a.div()