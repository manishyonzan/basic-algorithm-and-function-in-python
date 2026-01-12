# def calculate_pay(employee):
#     match employee.type:
#         case 'fullTime':
#             return employee.salary / 12
#         case 'partTime':
#             return employee.hours * employee.rate
#         case 'contractor':
#             return employee.hours * employee.contractRate
#         case _:
#             return "Invalid number"
        

# print(calculate_pay(3))



# and to generateRoport we have to use the same switch/ match logic in every function repeating, and add new case for each type and so dont repeat yourself and use polymorphism 

class Contractor:
    def __init__(self,data):
        pass
    def generate_report(self):
        print("contractor generating report")
        pass
    def salary(self):
        print("contractor salary is ...")
        
class FullTime:
    def __init__(self,data):
        pass
    def generate_report(self):
        print("fulltime generating report")
        pass
    def salary(self):
        print("fulltime salary is ...")
        
class PartTime:
    def __init__(self,data):
        pass
    def generate_report(self):
        print("part time generating report")
        pass
    def salary(self):
        print("part time salary is ...")
            
            
    
def deposit(emp_id, data):
    print("emp id",emp_id,"with salary",data ) 
           
def functionPayroll(emp):
    # salary = emp.salary
    salary = 4
    deposit(emp_id=1,data=salary)
    


class EmployeeFactory:
    def __init__(self):
        pass
    def create(self,type, data):
        match type:
            case 'fulltime':
                return FullTime(data)
            case "contractor":
                return Contractor(data)
            case _:
                return PartTime(data)
            
factory = EmployeeFactory()

parttime = factory.create('parttime', {})
parttime.generate_report()     
functionPayroll(parttime)   