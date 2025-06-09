a = "hello"

print(a)

a = '''hellow
jdjdjdjdjd '''

print(a)


# strings are array
a = "hello world"
print(a[2])

# looping through string
for x in "banana":
    print(x)
    
a ="Hello world"
print(len(a))


txt = "the best things in life are free"
print("best" in txt)


if "free" in txt:
    print("Yes there is freee in txt")
    
print("expensive" not in txt)


if "expensive" not in txt:
    print("No, expensive is not present")
    
    
b = "hello world"
print(b[2:5])   # 5 index  is not included which is 6 sequentially starting from 0

# slice from the start

print(b[:5])

# slice to the end

print(b[2:])

# negative indexing to start the slice from the end of the string:

print(b[-5:-2])


# slicing

a = "Hello, World!"
print(a.upper())

print(a.lower())

a = " Hello world "
print("a:"+a,"a:"+a.strip())


a = "Hello, World!"
print(a.replace("He", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# age = 36
# txt = "My name is John, I am " + age
# print(txt)                we cannot combine int and str like this

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

