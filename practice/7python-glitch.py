# is vs ==
print("is v ==")
a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)


# mutable defaults can cause problem, default variables like int, string not a problem
print("mutable defaults")
def add_element(element, my_list = []):
    my_list.append(element)
    return my_list
print(add_element(5))
print(add_element(6))

# duck typing, python uses  duck typing where the type of object is based on the behaviour rather than inheritence. this can lead to unexpected behavious if we assume types
print("duck typing")
class Duck:
    def quack(self):
        return "Quack"
class Dog:
    def quack(self):
        return "I am a dog but i can quack"
    
# chained assignment, variables can be assigned in chain it is confusing if the underlying data type is mutable
print("chained assignment")
a = b = []
a.append(1)
print(b)

# closures and late binding: pythons closures can behave unexpectedly due to late binding where variables are resolved when a function is called , not when its defined

funcs = [lambda x: x + i for i in range(3)]

print([f(10) for f in funcs])


