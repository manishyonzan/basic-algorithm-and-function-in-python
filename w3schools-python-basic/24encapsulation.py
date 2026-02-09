# encapsulation is about protecting data inside a class
# it means protecting the data (properties) and methods   together in a class while controlling how the data can be accessed from outside the class
# this prevents accidental changes to your data and hides the internal details of how the class works

class Animal:
    def __init__(self, name, birthdate):
        self.name = name
        self.__birthdate = birthdate
        
    def get_date(self):
        return self.__birthdate
    
    
a = Animal("hari", "2000-12-12") 

print(a.get_date())