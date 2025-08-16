import pandas as pd
from sklearn import linear_model

df = pd.read_csv("csv/data.csv")

X = df[['Weight', 'Volume']]

y = df[['CO2']]

model = linear_model.LinearRegression()
model.fit(X,y)

prediction = model.predict([[2300,1300]])

print("the prediction for 2300 weight and 1300 volume is ", prediction," of co2")

"""the coefficient values of the regression object:"""
print(model.coef_) #[[0.00755095 0.00780526]]

# The result array represents the coefficient values of weight and volume.

# Weight: 0.00755095
# Volume: 0.00780526

# These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.

# And if the engine size (Volume) increases by 1cm3, the CO2 emission increases by 0.00780526g.
