# https://pynative.com/python-basic-exercise-for-beginners/ 

# exercise 1:
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.


number1 = int(input("please enter the first number:"))
number2 = int(input("please enter the second number:"))

def calculaterules(number1, number2):
    multiplication = number2 * number1
    if multiplication <= 1000:
        return multiplication
    else:
        return number1 + number2
    
print('the result is', calculaterules(number1,number2))





# exercise 2: Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.


def printrange(rangenum):
    print(f"Printing the current and previoous number sum in  a range of {rangenum}")
    previousnum = 0
 
    for i in range(rangenum):
       
        print(f"the current num is{i}, the previous num is {previousnum} and the sum is {previousnum + i}")
        previousnum = i
        
        
n = int(input("number from 1-10"))
printrange(n)



#exercise 3: Write a Python code to accept a string from the user and display characters present at an even index number.


def displayevenposition(user_str):
    print("Printing only the even postion strings")
    for i in range(0,len(user_str)-1,2):
        print(user_str[i])
        
        
user = input("Please provide text:")
displayevenposition(user)



# exercise 4: Write a Python code to remove characters from a string from 0 to n and return a new string.

def removechar(userstr,num):
    return userstr[num:]

print(removechar("pynative",2))


# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

number_x = [1,2,3,4,5,1]
number_y = [1,2,3,4,5,3]

def checksameval(arr):
    return True if arr[0] == arr[-1] else False

print(checksameval(number_x))
print(checksameval(number_y))


# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5


number_l = [1,2,5,10,20,3]

def div_by_5(lst):
    newlist = []
    for i in lst:
        if i % 5 == 0:
            newlist.append(i)
        else:
            pass
    return newlist

print("the list divisible by 5 is", div_by_5(number_l))

# Exercise 7: Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.


str_x = "Emma is good developer. Emma is a writer"
sub_str_x = "Emma"
def find_occurence_of_subsring(original, substring):
    occurence = 0
    for i in original.split(" "):
        if i == substring:
            occurence += 1
            
    return occurence



# or solution can be
# str_x = "Emma is good developer. Emma is a writer"
# use count method of a str class
# cnt = str_x.count("Emma")
# print(cnt)
#  Run
# Solution 2: Without the string method

# def count_emma(statement):
#     print("Given String: ", statement)
#     count = 0
#     for i in range(len(statement) - 1):
#         count += statement[i: i + 4] == 'Emma'
#     return count

# count = count_emma("Emma is good developer. Emma is a writer")
# print("Emma appeared ", count, "times")

print("The occurance of substring:", find_occurence_of_subsring(str_x, sub_str_x))





# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5



for i in range(1,6):
    for j in range(0,i):
        print(i, end="")
    # print("\n", end="")
    print("")
    
    
    
# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.


def palindrome(number):
    print("Original number:", number)
    
    original_num = number
    
    reverse_num = 0
    while number > 0:
        remider = number % 10
        reverse_num = (reverse_num * 10) + remider
        number = number // 10
        
    if reverse_num == original_num:
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
        
palindrome(1234321)
palindrome(1234323)


def is_palindrome(number):

  # Handle negative numbers (they are typically not palindromes)
  if number < 0:
    return False

  # Convert the number to a string
  original_string = str(number)

  # Reverse the string using slicing
  reversed_string = original_string[::-1]

  # Compare the original and reversed strings
  if original_string == reversed_string:
    return True
  else:
    return False

# Example usage:
print(is_palindrome(121))   # Output: True
print(is_palindrome(123))




# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.



list1 = [1,2,3,4,5]
list2 = [9,12,34,11,23]


def merge_two(first,second):
    
    new_list = []
    
    for i in first:
        if i%2 == 0:
            pass
        else:
            new_list.append(i)
    for j in second:
        if j%2 == 0:
            new_list.append(j)
        else:
            pass
    return new_list

print(merge_two(list1,list2))


