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


