x = lambda a : a + 10
print(x(5))  #15



x = lambda x,y : x*y
print(x(2,3))  # 6

x = lambda a,b,c : a + b + c
print(x(1,1,3)) # 5


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def func(n):
    return lambda x : x * n

mydoubler = func(2)

print(mydoubler(1))  # 4


mytripler = func(3)

print(mytripler(6))




