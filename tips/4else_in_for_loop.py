import random


# this else will run if the break never happens
price = 0
for i in range(random.randint(5,15)):
    print(i)
    price = price + 1
    if price == 4:
        print("Price reached 10")
        break
else:
    print("Price never reached 10")
    
    
# same for while loop , if break happens the else block donot run
    
i = 0

while i<3:
    print(i)
    i+=1
    if i==2:
        break
else:
    print("else block")