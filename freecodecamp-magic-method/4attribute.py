# getattr and getattribute
# Python provides two methods for controlling attribute access:

# __getattr__: Called only when an attribute lookup fails (that is, when the attribute doesn't exist)

# __getattribute__: Called for every attribute access, even for attributes that exist

class AttributeDemo:
    def __init__(self):
        self.name = "vivek"
        
        
    def __getattr__(self,name):
        print(f"__getattr__ called for {name}")
        return f"Default value for {name}"
    
        
    def __getattribute__(self, name):
        print(f"__getattribute__ called for {name}")
        return super().__getattribute__(name)
    # like some_object.foo—Python internally calls some_object.__getattribute__('foo'). This is how Python handles attribute access under the hood. 
    # so instead of calling the getattiute it will change to getattribute from the object so super(). calls the objects deffault function to avoid recursion

    
demo = AttributeDemo()

print(demo.name)    # __getattribute__ called for name                                
                    # vivek

print(demo.age)   #__getattr__ called for age   (it will be called if the __getattribute__ failed) 
                  #Default value for age 
                  
                  
                  
# setattr and delattr
# Similarly, you can control how attributes are set and deleted:

# __setattr__: Called when an attribute is set

# __delattr__: Called when an attribute is deleted                


print("\n \n")


# These methods let you implement validation, logging, or custom behavior when attributes are modified.


import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# - level=logging.INFO sets the minimum severity of messages to handle. 
# INFO means it will show info messages, warnings, errors, and critical issues (but not debug messages)

# - format='%(asctime)s - %(levelname)s - %(message)s' tells Python how to format the log messages. This one includes:
# - asctime: the timestamp of the log
# - levelname: the level (INFO, WARNING, etc.)
# - message: the actual message you log


class LoggedObject:
    def __init__(self, **kwargs):
        self._data = {}
        # Initialize attributes without triggering __setattr__
        for key, value in kwargs.items():
            self._data[key] = value
            
            
    def __getattr__(self,name):
        if name in self._data:
            logging.debug(f"Accessing attribute {name}: {self._data[name]} ")
            return self._data[name]
        
        raise AttributeError(f" '{self.__class__.__name__} object has no attribute {name}' ")
    
    def __setattr__(self, name, value):
        print(name,"the name")
        if name == "_data":
             # Allow setting the _data attribute directly
            super().__setattr__(name,value)
            
        else:
            old_value = self._data.get(name, "<undefined>")
            self._data[name] =  value
            logging.info(f"Changed {name}: {old_value} -> {value}")
            
    def __delattr__(self, name):
        if name in self._data:
            old_value = self._data[name]
            del self._data[name]
            logging.info(f"Deleted {name}: (was :{old_value})")
        else:
            raise AttributeError(f" {self.__class__.__name__}' object has no attribute '{name}'")
        
        
user = LoggedObject(name="vivek", email = "hello@wewake.dev")

# Modify attributes
user.name = "Vivek"  # Logs: Changed name: Vivek -> Vivek
user.age = 30  


# Access attributes
print(user.name)      # Output: Vivek


# Delete attributes
del user.email  


try:
    print(user.email)
except AttributeError as e:
    print("AttributeError:" ,{e})