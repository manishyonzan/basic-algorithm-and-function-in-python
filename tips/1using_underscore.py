# using _ for number to make it more readable

value = 2_00_000
hexval = 0x_54_fa
binary = 0b_01_01
operations = 1_234 * 1_999
print(value,hexval,binary,operations)

# using in throw away variable

name,_,age = ["bob",2000,23]
print(name,age)

first, *_,last = [1,2,3,4,5,6,7,8]

print(first,last)

for _ in range(3):
    print("val")