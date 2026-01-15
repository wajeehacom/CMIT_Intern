class Student:
    def set_name(obj, name):
        obj.name = name

    def show(obj):
        print(obj.name)

s = Student()
s.set_name("Wajeeha")
s.show()

# using self
class A:
    def show(self):
        print("Hello")

a = A()
a.show()
# __str__() method
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"

s = Student("Wajeeha")
print(s)
# polymor
# Base class
class Animal:
    def speak(self):
        print(" animal sound")
class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")
a1 = Dog()
a2 = Cat()

animals = [a1, a2]

for animal in animals:
    animal.speak()
