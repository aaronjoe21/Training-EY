'''
class Mathops:
    def add(self,a,b=0,c=0):
        return a + b + c
m=Mathops()
print(m.add(5))
print(m.add(5,6))
print(m.add(5,6,7))
'''

class Mathops:
    def add(self,*args):
        return sum(args)
m=Mathops()
print(m.add(5,6,7))
print(m.add(5,6,7,8,9))
print(m.add(5,6,7,8,9,10))