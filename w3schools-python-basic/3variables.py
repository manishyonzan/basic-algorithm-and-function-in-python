from itertools import tee
import keyword


x = 4  #it is a type of int
y = 'John' # it is a type of str

print(x)
print(y)


                    
# Casting

a = str(3) # x will be '3';
b = int(3) # b will be 3;
c = float(3) # c will be 3.0;

# get the type                   

print(type(a),"is the type of a")
print(type(b),"is the type of b")
print(type(c),"is the type of c")


# single or double quotes are same

d = 'hello'
# is same as
d = "hello"


# case sensitive : variables name are case sensitive

e = 6
E = 'hello world'
# E will not overwrite e


# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# illegal variables name

# 3var = 3
# my-var = 'djdj' 
# my var = 'sss'





# Assign many values to multiple variables

x,y,z  = 'first', 'second', 'third'

print(x,y,z)


# one value to multiple variables

x = y = z = 19

print(x,y,z)


# unpack  a collection
# x,y,z = [1,2,3,3] if the variable and item equal but if has more then use * as x,y,*z or *x,y,z
x,y,*z = [1,2,3,3]

print(x,y,z)



x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"

# the + will not add space " " between values

print(x + y + z)


x = 5
y = 10
print(x + y)

x = 5
y = "John"
# print(x + y) this will give error as we try to combine a string and number in such case use comma

print(x,y)


# Global variables

x = 'awesome'

def myfunc():
    print("python is " + x )
    
myfunc()

x = 'awesome'

def myfunc():
    x = 'fantastic'
    print('python is ' + x)
    
myfunc()
print('python is ' + x)

# using the gobal keyword

def myfunc():
    global x
    x = 'fantastic 2'
    print('Python is' + x)
    
myfunc()
    
print('python is ' + x)
