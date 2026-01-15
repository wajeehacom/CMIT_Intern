#class attributes
"""
class Employee:
    count=0
    def __init__(self,name):
        self.name=name
        Employee.count +=1
        print("Employee's Name:",self.name,"No of employee:",Employee.count)

e1 =Employee("Wajeeha Yaseen")
print()
e2=Employee("Maria")
"""
#class variables
"""
class Employee:
    count=0
    def __init__(self,name):
        self.name=name
        Employee.count +=1
        print("Employee's Name:",self.name)

    def print_count():
        print("No of employee:",Employee.count)    

e1 =Employee("Wajeeha Yaseen")

e2=Employee("Maria")
e3=Employee("Ayesha")
e4=Employee("Ali")
Employee.print_count()

"""

# class method, or class decorator
"""
class Employee:
    count=0
    def __init__(self,name):
        self.name=name
        Employee.count +=1
        print("Employee's Name:",self.name)
    @classmethod    
    def print_count(cls):
        print("No of employee:",cls.count)    

e1 =Employee("Wajeeha Yaseen")

e2=Employee("Maria")
e3=Employee("Ayesha")
e4=Employee("Ali")
Employee.print_count()

"""
# alternative constructors
"""
class Employee:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Employee.count +=1
        print("Employee's Name:",self.name,"age:",self.age)
        print("no of employee:",Employee.count)

    @classmethod    
    def alternative_contructor(cls,data):
        name,age=data.split("-")
        return cls(name,int(age))
       # this is way to create the object

        

e1 =Employee("Wajeeha Yaseen",12)

e2=Employee("Maria",23)
e3=Employee("Ayesha",45)
e4=Employee("Ali",78)
e5= Employee.alternative_contructor("Zain-12")
print("Name after split:",e5.name,"age after spliting:",e5.age)
"""
# setattr function dynamically create the object attributes
"""
class Person:
    pass


p= Person()
setattr(p,"name","Wajeeha Yaseen")
setattr(p,"age",23)
print(p.name)
print(p.age)
"""
# static method
"""
class Circle:
    pi=3.145
    def __init__(self,radius):
        self.radius=radius
    
    @staticmethod
    def calculateArea(radius):
         return Circle.pi* radius**2
    
c=Circle(10)
print(Circle.calculateArea(10))
"""
#diff static or class methos hoome task

"""

class Employee:
    count=0
    company_name="Grayphite"
    def __init__(self,name, age):
        self.name=name
        self.age=age
        Employee.count+=1
    @classmethod
    def showInfo(cls):
        print("Total No of Employee:",cls.count)

    def employeeInfo(self):
        print("Employee Name:",self.name,"Employee Age:",self.age)    


    @staticmethod
    def isValideAge(age):
        return age>=18
    
class Manager(Employee):
    def __init__(self,name,age,level):
        super().__init__(name,age)
        self.level=level
    
    def manager_detail(self):
        
        if self.isValideAge(self.age):
          super().employeeInfo()

          print("Level:",self.level)
        else:
            print("Invalid,age should be greater than or equal to 18")  
         
e1 = Employee("Wajeeha", 23)
m1 = Manager("Maria", 28, 8)



m1.manager_detail() 

"""

#positional arguments


"""
class Person:
    def __init__(self,*args):
        if(len(args))==1:
            self.name=args[0]
        elif(len(args))==2:
            self.name=args[0]
            self.age=args[1]
        elif(len(args))==3:
            self.name=args[0]
            self.age=args[1]
            self.country=args[2]
        else:
            print("end")    
p=Person("Wajeeha")     
print(p.name)
p1=Person("Ayesha",23,"Burewala")
print("name:",p1.name,"Age:",p1.age,"Country:",p1.country)
"""

#Access Specifier

"""
class Person:
    def __init__(self):
        self.name="Wajeeha"
        self._age=34 #protected
        self.__country="Pakistan" #private
    def getCountry(self):
        return self.__country
class Detail(Person):
    def showDetailOfPerson(self):
        print("Name",self.name,"age is:",self._age,"Country:",self.getCountry())   
             


d=Detail()
d.showDetailOfPerson()

"""
#DSA in python
#Searching Algorithm in python
"""
my_list=[23,25,1,9,-1]
minVal=my_list[0]
for i in my_list:
    if i<minVal:
        minVal=i
print("Lowest Element :",minVal)
"""
#array


import array as arr
my_arr=arr.array('i',[1,2,3])
# if we will use or write simply,i in my_arr, so arry will be go to out of range
for i in range(len(my_arr)): 
 print("Element at Index",i,":",my_arr[i])