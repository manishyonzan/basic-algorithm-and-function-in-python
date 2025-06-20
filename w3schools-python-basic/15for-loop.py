fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
    
for letter in 'banana':
    print(letter, end=" ")
print("\n")


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    if fruit == 'banana':
        break
    
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == 'banana':
        continue
    print(fruit)   #output apple cherry 
    
    
for x in range(6):
    print(x) # 0 1 2 3 4 5
    
    
for x in range(2, 6):
    print(x) # 2,3,4,5
    
    
# Increment the sequence with 3 (default is 1): by adding 3 in the third parameter
for x in range(2, 30, 3):
    print(x)  #2 5,8,11....29


# Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(6):
    print(x)
else:
    print("Finally finished!")
    
    
for x in range(6):
    if x ==3: break
    print(x)
else:
    print("Finally finished")   #this will not print as it break before the for loop ended
    
    

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]


for x in adj:
    for y in fruits:
        print(x,y)
        
# output

# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry


# for loop cannot be empty so to avoid the error we can use pass keyword
for x in [0, 1, 2]:
  pass