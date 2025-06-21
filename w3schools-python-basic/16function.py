def my_function():
    print("Hello from a function")
    
my_function()



def my_funciton(name):
    print(f"{name} is my name")
    
my_funciton("messi")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")  # it is a problem because you passed 1 argument and it has 2 parameters



# to pass a list kind of data
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.


def my_function(child3, child2, child1):
    
    """
    Adds two numbers together.

    Parameters:
        child1 (string): The first child name.
        child2 (string): The second child name.
        child3  (string): The third child name.
        

    Returns:
        none: Print the text.
    """

    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")




# default parameter

def my_function(country = "Norway"):
  print("I am from " + country)

my_function() #I am from Norway
my_function("Brazil") #I am from Brazil


def my_funciton(food):
    for x in food:
        print(x)
        
        
fruits = ['apple', 'banana', 'pineapple']

my_funciton(fruits)



# return values

def my_function(x):
  return 5 * x

print(my_function(3)) # 15



# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

# To specify that a function can have only positional arguments, add , / after the arguments:


def my_function(x,/):
# def my_function(x, /,y): we can also use this

  print(x)

my_function(3)


# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
    
def my_function(x):
  print(x)

my_function(x = 3)


def my_function(*, x):
  print(x)

my_function(x = 4)


def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)




def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)



# hashable -> list are hashable so they need to be converted to tuple before making same value for comparison in set

def check_set(x):
    return set(tuple(i) for i in x)


print(check_set([[1,2,3], [1,2,3]]))

