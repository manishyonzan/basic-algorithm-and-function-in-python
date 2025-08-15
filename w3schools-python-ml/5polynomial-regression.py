"""

Python has methods for finding a relationship between data-points and to draw a line of polynomial regression. 
In the example below, we have registered 18 cars as they were passing a certain tollbooth.

We have registered the car's speed, and the time of day (hour) the passing occurred.

The x-axis represents the hours of the day and the y-axis represents the speed:

"""

import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))


"""
print(mymodel) this model is function (polynomial) not the value like in linear regression and it is 

          3         2
-0.03032 x + 1.343 x - 15.54 x + 113.8

"""
# myline = numpy.linspace(1, 20, 100) #the line will start from 1 to 20
myline = numpy.linspace(1, 22, 200)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()


# check how well the data fits in a polynomial regression
# it gives values from 0-1 as percentage
print(r2_score(y, mymodel(x)))