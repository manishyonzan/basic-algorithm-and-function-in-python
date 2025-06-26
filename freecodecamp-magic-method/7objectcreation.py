# The __new__ method is called before __init__ and is responsible for creating and returning a new instance of the class.
# This is useful for implementing patterns like singletons or immutable objects.

class Singleton:
    _instance = None
    
    def __new__(cls,*args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name=None):
        if name is not None:
            self.name = name
        
        
#usage
s1 = Singleton("Vivek")
s2 = Singleton("Wewake")

print( s1 is s2)   #True as it is the same object
print(s1.name) #Wewake because it replaces 

# Let's break down how this singleton works:

# Class variable: _instance stores the single instance of the class

# new method:

# Checks if an instance exists

# Creates one if it doesn't

# Returns the existing instance if it does

# init method:

# Called every time the constructor is used

# Updates the instance's attributes