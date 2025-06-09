mylist = ['apple','banana', 'cherry']

print(mylist)

# length of list

print(len(mylist))

list2 = [True, "jdjd", 5, True]

print(list2)
print(type(list2))

# using the list() constructor to make the list

mylist = list((3,"jfjf"))

print(type(mylist),mylist)


# access item from list

try:
    a = mylist[2]
except IndexError:
    print("imdex out of range")
except Exception as e:
    print(f'an error occured:{e}')
else:
    print('some error ocurred')
finally:
    print('finally')
    
    


mylist = ['apple', 'banana', 'cherry']
print(mylist[-1], 'the last item of list')


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

chek = 'apple '
if chek.strip() in thislist:
    print('the apple is in the list')
else:
    print("apple is not in the list")
    
    
    
    
    
# change item in the list
thislist = ["apple", "banana", "cherry"]

thislist[1] = 'avacado'
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]

def changelist(first, second, toadd, original):
    if second-first != len(toadd):
        print("total list number do not match with range given")
    else:
        original[first:second] = toadd
        print("Updated")
        
changelist(1,3,["blackcurrant", "watermelon"], thislist)
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# insert item without removing remaining item

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']



# add list item

thislist = ["apple", "banana", "cherry"]

thislist.append('avacado')

print(thislist)



# extend the new list

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
thislist.extend({'name':"messi", 'prof':"player"})

print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange', 'name', 'prof']


# remove item from list

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry', 'banana', 'kiwi'] removed first occurence of banana

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana'] removes from last item

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) NameError: name 'thislist' is not defined

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[] empties the list


# python loop list

thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)
    
    
for x in range(0,len(thislist)):
    print(thislist[x])
    
i = 0
while i < len(thislist):
    print(thislist[i])
    i+=1

[print(x) for x in thislist]


# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for a in fruits:
    if 'a' in a:
        newlist.append(a)
        
print(newlist)


# using list comprehension

newlist = [x for x in fruits if 'a' in x]

print(newlist, 'using list comprehension')

newlist = [x for x in fruits if x != "apple"]
print(newlist)


newlist = [x.upper() for x in fruits]
print(newlist) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist) #['apple', 'orange', 'cherry', 'kiwi', 'mango']





# sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()

print(thislist)  #['banana', 'kiwi', 'mango', 'orange', 'pineapple']


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse= True) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']

print(thislist)


# customizing the sorting using key

def custom_sort(n):
    return abs(n-50)

thislist = [100,200,50,55,78,66,12]

thislist.sort(key=custom_sort) #[50, 55, 66, 78, 12, 100, 200]

print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry'] is it is better to choose key as lower

thislist.sort(key=str.lower)

print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()

print(thislist)


# copy a list

thislist = ["apple", "banana", "cherry"]
new_copy = thislist.copy()
print(new_copy,'the copy')

# copy using list method

new_copy = list([*thislist,'hello'])  

print(new_copy)  #['apple', 'banana', 'cherry', 'hello']

new_copy = thislist[:]

print(new_copy) #['apple', 'banana', 'cherry']

    
    # join list

list1  = ['a', 'b', 'c']
list2 = [ 1,2,3]

list3 = list1 + list2

print(list3)

for x in list1:
    list2.append(x)
    
print(list2)


list1.extend(list2)
print(list1)


