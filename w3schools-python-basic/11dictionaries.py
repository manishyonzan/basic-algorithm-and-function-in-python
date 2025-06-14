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


