ram = "hello".format
print(ram)

hari = "hello {}".format("hari")
print(hari)
a = "{} {} {}".format("first","second","third")
print(a)

d= "{2} {0} {1}".format("first", "second","third")
print(d)
e = "{a} {b} {c}".format(a="first",b="second",c="third")
print(e)

# f ="{2} {0} {}".format("first","second","third")
# it wont work

# however below code will work
f ="{1} {0} {last}".format("first","second",last="third")
print(f)


# the topic in the course is 
# the <name> and <conversion> component

example_dict = {
    "name":"lian",
    "age":"old",
    "height":"kinda tall"
}
example_dict2 = {
    "name":"liam",
    "age":"old",
    "height":"kinda tall"
}

g =  "{0[name]} {1[name]}".format(example_dict,example_dict2)
print(g)

h = "{d[name]}".format(d=example_dict)
print(h)





class container():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return "repr of container"
    def __str__(self) -> str:
        return "Str of container"
    
c = container(5,6)
print("{}".format(c))
print("{0.x}".format(c))
print("{c.y}".format(c=c))
print("{!r}".format(c))
print("{!s}".format(c))
print("{!a}".format(c))

print("{0.x!r}".format(c))
print("{0.x!s}".format(c))