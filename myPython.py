"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def std_Info(self):
        print("Name:",self.name,"Age:",self.age)
 
s=Student("Wajeeha",12)
print(s.std_Info())
       """

# polymorhism
"""
class Animal:
    def speak(self):
        print("Animals are speaking")
class Cat(Animal):
    def speak(self):
        print("Meo!")
class Dog(Animal):
    def speak(self):
        print("Woof!")
       
    

d=Dog()
print(d.speak())
"""
#exmaple

"""
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

def print_area(shape):
    print("Area:", shape.area())

# Test
r = Rectangle(5, 10)
c = Circle(7)

print_area(r)  
print_area(c)  

"""


# File handling
#f= open("demo.txt",'r')
#print(f.read()) if we use it , we need to close it
           
with open("demo.txt",'r') as f:
    print(f.read())

