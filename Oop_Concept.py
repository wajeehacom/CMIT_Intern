class Student:
    def set_name(obj, name):
        obj.name = name

    def show(obj):
        print(obj.name)

s = Student()
s.set_name("Wajeeha")
s.show()
