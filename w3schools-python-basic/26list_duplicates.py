mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))

print(mylist)



# function where you can send list and get them without duplicates 

def myfunction(x):
    return  list(dict.fromkeys(x))

mylist = myfunction([*mylist, "e"])
print(mylist)


# reverse a string
text = "Hello World" [::-1]
print(text)


def reverse_str(x):
    return x[::-1]


mytxt = reverse_str("my string is this and what is this")
print(mytxt)



# print two number

x = 5
y = 9

print(x + y)

x   = input("enter a value for x")
y  = input("enter a value for y")

print(int(x) + int(y))
