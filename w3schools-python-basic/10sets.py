myset = {"apple", "banana", "cherry"}

# sets donot have order and cannot be accessed using index like variable[0], Set items are unordered, unchangeable, but you can remove and add items and do not allow duplicate values.

print(myset)

thisset = {"apple", "banana", "cherry", 1, 2}

print(thisset) #{1, 2, 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) #{'banana', 2, True, 'apple', 'cherry'}   because True and 1 is considered same and which ever comes first is taken and other is removed as it doesnot allow duplicate

thisset = {"apple", "banana", "cherry", False, True, 0} #same for False and 0

print(thisset)


thisset = {"apple", "banana", "cherry"}

print(len(thisset)) #3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(type(set1))  #<class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# loop through

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) #True


thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset) #False

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) #{'orange', 'apple', 'banana', 'cherry'} because it doesnot have order


# To add items from another set into the current set, use the update() method.  Add elements from tropical into thisset:


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)



# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
mydict = {"name":"hero"}

thisset.update(mylist)
thisset.update(mydict)
print(thisset)  #{'kiwi', 'orange', 'cherry', 'name', 'banana', 'apple'}


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) #{'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) #{'cherry', 'apple'}

 #If the item to remove does not exist, discard() will NOT raise an error.


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# The clear() method empties the set:
    
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)



thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets. union will return to variable, update will change the value of set
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)  #{1, 'a', 2, 3, 'c', 'b'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
 
 
# You can use the | operator instead of the union() method, and you will get the same result.

set3 = set1 | set2
print(set3) #{1, 2, 3, 'b', 'a', 'c'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)  #{1, 2, 3, 'bananas', 'a', 'cherry', 'John', 'c', 'b', 'Elena', 'apple'}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) #{1, 2, 3, 'bananas', 'a', 'cherry', 'John', 'c', 'b', 'Elena', 'apple'}


x = {"a", "b", "c"}
y = (1, 2, 3)
mydict = {"name":"hero"}
z = x.union(y,mydict)
print(z) #{1, 2, 3, 'a', 'c', 'b', 'name'}


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
# The update() method inserts the items in set2 into set1:
set1.update(set2)
print(set1)



set1 = {"apple", "banana", "cherry"}
set2 = {"google":"", "microsoft":"", "apple":"dd"}

# The intersection() method will return a new set, that only contains the items that are present in both sets.  it will in other data collection like list, tuple, dictionary


set3 = set1.intersection(set2)
print(set3) # apple



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

set3 = set1 & set2
print(set3)   #apple



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}


# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1.intersection_update(set2)
print(set1)



set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
# The values True and 1 are considered the same value. The same goes for False and 0.
set3 = set1.intersection(set2) 

print(set3) #{False, 1, 'apple'}

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) #{'banana', 'cherry'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# You can use the - operator instead of the difference() method, and you will get the same result.
# The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
set3 = set1 - set2
print(set3) #{'banana', 'cherry'}

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
# Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1) #{'banana', 'cherry'}




# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)  #{'cherry', 'google', 'banana', 'microsoft'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
set3 = set1 ^ set2
print(set3) #{'cherry', 'google', 'banana', 'microsoft'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1) #{'cherry', 'google', 'banana', 'microsoft'}