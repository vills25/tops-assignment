# 22. How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.
"""
Syntax of class : 

    class class_name:
        Data memebers

        Member functions

    Syntax of object:
    instance_name = class_name([paras])

--> What Is Self?
    Self represents the instance of the class. By using the “self” we can access the attributes and methods of the class in Python.
    It binds the attributes with the given arguments
    
--> Example Of A Python Class: 

class demo:
    # data member
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))


    # member function
    def student(self):
        print("I am a student")

# create object
s = demo()
print(s.name)
print(s.age)
s.student()    
       
"""
##################################################################################################################################################

# 23. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  #l*w

length = 5
width = 10

rectangle = Rectangle(length, width)

print("Area of the rectangle:", rectangle.area())
"""

##################################################################################################################################################

# 24. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
"""
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2 # πr2

    def perimeter(self):
        return 2 * math.pi * self.radius # 2πr

radius = 7

circle = Circle(radius)

print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())
"""
##################################################################################################################################################

# 25. Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
'''
inheritance allows you to reuse code and create more complex and organized programs.

there are 4 types of inheritance in python.

(1) Single inheritance --> A childe class can inherit from only one parent class.

class animal:
    def speak(self):
        print("Animal speaking")
        
class dog(animal):
    def bark(self):
        print("Dog is barking")
               
d = dog()
d.bark()
d.speak() 

(2) Multiple inheritance --> A Child class can inherit from multiple parent classes.

class animal:
    def speak(self):
        print("Animal speaking")
        
class dog:
    def bark(self):
        print("Dog is barking")
        
class eat(dog,animal) :
    def eat(self):
        print("Eating")              
d = eat()

d.bark()
d.speak()
d.eat()

(3) Multi_level inheritance --> A child class can inherit from parent class that inherits from another parent class.

class animal:

    def speak(self):
        print("Animal speaking")
        
class dog(animal):
    def bark(self):
        print("Dog is barking")
        
class eat(dog) :
    def eat(self):
        print("Eating")  
                    
d = eat()
d.bark()
d.speak()
d.eat()

(4) Hierarchical inheritance --> Multiple child classes inherit from a single parent class.

class animal:

    def speak(self):
        print("Animal speaking")
        
class dog(animal):
    def bark(self):
        print("Dog is barking")
        
class eat(animal):
    def eat(self):
        print("Eating")   
                   
d = eat()
d.bark()
d.speak()
d.eat()

--> What is init?
   The __init__ method also known as Constructor.
   This method called when an object is created from the class and it allow the class to initialize the attribbutes of a class.
   The python __init__ method is declared within a class and is used to initialize the attributes of an object as soon as the object is formed.

--> What is Python Constructor
In Python, a constructor is a special method that is called when an object is created. The purpose of a python constructor is to assign values to 
the data members within the class when an object is initialized. The name of the constructor method is always __init__.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
person=person("Vishal", 21)
print(person.name)
print(person.age) 
   '''
##################################################################################################################################################


    
