thistuple   = ( 'apple', 'cherry', 'banana', 'apple')
print(thistuple)

print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))  #<class 'tuple'> 

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))  #<class 'str'> because there is no comma after the item if only one item is present



tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #('apple', 'banana', 'cherry')

# access tuple items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #banana

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  #cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  #('cherry', 'orange', 'kiwi')

print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:]) # ('cherry', 'orange', 'kiwi', 'melon', 'mango')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
  
  

# change tuple values although it is a unchangeable data types

x = ("apple", "banana", "cherry")
y = list(x)
y[0] = "watermelon"
x = tuple(y)
print(x) #('watermelon', 'banana', 'cherry')

# add a value to tuple

y = list(x)
y.append('orange')
x = tuple(y)
print(x) #('watermelon', 'banana', 'cherry', 'orange')

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

newtuple = ('lichi', 'guava')

x += newtuple
print(x) #('watermelon', 'banana', 'cherry', 'orange', 'lichi', 'guava')

# to delete also same convert to list and the remove

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #('banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists



fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) # apple
print(tropic) #['mango', 'papaya', 'pineapple']
print(red) #cherry

# loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
  
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  #('a', 'b', 'c', 1, 2, 3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)  #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)  #2

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x) #3 which was the first occurance




  