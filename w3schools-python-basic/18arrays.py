import numpy as np

x = np.array([1,2,3])
print(x) # [1 2 3]

print(x[0]) # 1

x[0] = 5
print(x) #[5 2 3]

print(len(x))

for i in x:
    print(i)
    