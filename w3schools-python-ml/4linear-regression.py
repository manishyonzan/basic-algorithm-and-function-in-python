import matplotlib.pyplot as plt
from scipy import stats


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


slope,intercept,r,p, std_err = stats.linregress(x,y)


""" the relation ship between x and y values"""
print(r)


def myfunc(x):
    return slope * x + intercept

"""predict the value of y if the x value is 10"""
future = myfunc(10)
print(future)




mymodel = list(map(myfunc,x))

# the mymodel is the prediction of y based on the relationship learn from the x and y, so it can also be said as y value

plt.scatter(x,y)
plt.plot(x,mymodel)

plt.show()

