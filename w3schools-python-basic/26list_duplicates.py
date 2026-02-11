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