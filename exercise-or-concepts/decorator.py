import time 
import math

def calculate_time(func):
    def inner1(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print("Total time taken in:",func.__name__,end - begin)
    return inner1

       
@calculate_time
def factorial(num):
    print(math.factorial(num))
    
factorial(10)


# What if a function returns something or an argument is passed to the function?

def decorator2(func):
    def inner1(*args,**kwargs):
        print("if need do something before execution")
        returned_value = func(*args,**kwargs)
        print("if need do something after execution")
        return returned_value
    return inner1

@decorator2
def sum_two_numbers(a,b):
    return a+b

a,b = 2,3
print("Sum:", sum_two_numbers(a,b))
