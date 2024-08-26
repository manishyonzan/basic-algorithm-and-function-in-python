ram = "hello".format
print(ram)

hari = "hello {}".format("hari")
print(hari)
c = "{} {} {}".format("first","second","third")
print(c)

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