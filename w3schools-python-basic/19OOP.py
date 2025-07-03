class MyClass:
    x = 5
    
p1 = MyClass()

print(p1.x)
print(MyClass.x)



class Person:
    def __init__(self,name:str, age:int) -> None:
        self.name = name
        self.age = age
        
p1 = Person("John", 36)
        
print(p1.name)
print(p1) # <__main__.Person object at 0x000001EE8C3158D0>

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:


class Person:
    def __init__(self,name:str, age:int) -> None:
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} : {self.age}"
    
            
p1 = Person("John", 36)

print(p1)  #John: 36



class Person:
    def __init__(self,name:str, age:int) -> None:
        self.name = name
        self.age = age
        
    def my_func(self):
        print(f"Hello, My name is {self.name}")
        
p1 = Person("John", 36)

# x = p1.my_func
# x()
# is same as
p1.my_func() # Hello, My name is John


# modify object properties
p1.name = "Hari"
p1.my_func()  #Hello, My name is Hari



# delete object property

del p1.name

# p1.my_func()  #AttributeError: 'Person' object has no attribute 'name'


del p1

# p1.my_func()  #NameError: name 'p1' is not defined




# What are Magic Methods?
# Magic methods in Python are special methods that start and end with double underscores (__).
# When you use certain operations or functions on your objects, Python automatically calls these methods.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + self.y)
    
    def __str__(self):
        return f"{self.x},{self.y}"
    
p1 = Point(1,1)
p2 = Point(2,2)

p3 = p1 + p2
print(p3.x, p3.y) #3 2

print(p3)  # 3, 2
print(str(p3))  # 3, 2



# __str__ returns a user-friendly string showing the temperature with a degree symbol

# __repr__ returns a string that shows how to create the object, which is useful for debugging

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
    
    def __str__(self):
        return f"{self.celsius}°c"
    
    def __repr__(self):
        return f"Temperature({self.celsius})"
    
temp = Temperature(25)
print(str(temp))
print(repr(temp))






        




