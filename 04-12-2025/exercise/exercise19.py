
class Vehicle:
    def max_speed(self):
        return "Speed varies"

class Car(Vehicle):
    def max_speed(self):
        return "Car max speed: 180 km/h"

class Bike(Vehicle):
    def max_speed(self):
        return "Bike max speed: 120 km/h"

# Test
v = Vehicle()
c = Car()
b = Bike()
print(v.max_speed())
print(c.max_speed())
print(b.max_speed())
