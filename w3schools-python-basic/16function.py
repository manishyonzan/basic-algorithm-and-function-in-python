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


