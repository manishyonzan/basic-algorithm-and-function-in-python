def calculate_pay(employee):
    match employee.type:
        case 'fullTime':
            return employee.salary / 12
        case 'partTime':
            return employee.hours * employee.rate
        case 'contractor':
            return employee.hours * employee.contractRate
        case _:
            return "Invalid number"
        
        
# and to generateRoport we have to use the same switch/ match logic in every function repeating, and add new case for each type and so dont repeat yourself and use polymorphism 


        
print(calculate_pay(3))