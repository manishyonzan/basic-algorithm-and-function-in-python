import numpy
# from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)


median = numpy.median(speed)
print(median)

# mode = stats.mode(speed)
# print(mode)


# standard deviation

speed = [86,87,88,86,87,85,86]

standardDevation = numpy.std(speed)

print("standard deviation:", standardDevation)


# variance

variance = numpy.var(speed)

print("variance:",variance)




# Use the NumPy percentile() method to find the percentiles:

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print("75 percentile",x)


ninetyPercentile = numpy.percentile(ages, 90)

print("ninetyPercentile:", ninetyPercentile)