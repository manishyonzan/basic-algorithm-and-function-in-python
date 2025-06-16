thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) #Ford


print(len(thisdict)) #3


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(type(thisdict)) #<class 'dict'>

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)  #{'name': 'John', 'age': 36, 'country': 'Norway'}
x = thisdict.get("name")
print(x) #John


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x, 'these are the keys') #before the change  output: dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change  output: dict_keys(['brand', 'model', 'year', 'color'])
#it is iterable
# for a in x:
#     print(a)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change output: dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change output:dict_values(['Ford', 'Mustang', 2020])





car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change  output:dict_values(['Ford', 'Mustang', 1964, 'red'])



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020

print(x) #after the change -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change  -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["color"] = "red"

print(x) #after the change  -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
  
  
  
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


thisdict.update({"year": 2020})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "blue"})

print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'blue'}


# remove from a dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) #{'brand': 'Ford', 'year': 1964}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang'}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)  #{'brand': 'Ford', 'year': 1964}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict)   #NameError: name 'thisdict' is not defined


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)  #{}



# loop dictionary


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x) #print keys
  
  
for x in thisdict:
    print(thisdict[x]) # print values
    
    
    
for x in thisdict.values():
  print(x, end="") #FordMustang1964
  
print("\n")
for x in thisdict.keys():
  print(x, end="") #brandmodelyear
  
print("\n")
for x, y in thisdict.items():
  print(x, y)
# brand Ford
# model Mustang
# year 1964  

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
thisdict2 = thisdict
thisdict2['brand'] = "Honda"

print(thisdict) #{'brand': 'Honda', 'model': 'Mustang', 'year': 1964}
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}





# Nested dictionaries


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily) #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


print(myfamily)  #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}



print(myfamily["child2"]["name"])   #Tobias


for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
    
# child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011


