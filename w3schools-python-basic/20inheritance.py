class Person:
    def __init__(self,fname, lname):
        self.firstname = fname
        self.lastname = lname
        
        
    def printname(self):
        print(self.firstname, self.lastname)

peron1 = Person("john", "doe")
peron1.printname()  #john doe


class Student(Person):
    pass

student1 = Student("Hari", "bahadur")
student1.printname() #Hari bahadur


# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).

class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
        # to keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        # Person.__init__(self, fname, lname)
        
person2 = Student("j", "k")
person2.printname()



class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)

x.printname()
x.welcome()