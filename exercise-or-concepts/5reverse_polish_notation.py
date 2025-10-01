from math import ceil
# problem:given an array of strink tokens that represents
# arithmetic expression in a reverse polish notation evaluate the expression and return an integer that represents the value of the expression
# valid operators are +, -,/,*

# logic is  iterate and push item in the stack if you find expression pop last two and calculate and push in the stack

tokens1 = ["2", "1", "+", "3","*"]
output1 = 9
# explanation = (2+1) * 3 = 9

tokens2 = ['4','13','5','/','+']
output2 = 6
# explanation = (4 + (13/5)) = 6

def calculate_exp(token):
    stack = []
    exp = ['/','+', '-', '*']
    for each in token:
        if each in exp:
            a = int(stack.pop())
            b = int(stack.pop())
            if each =="+":
                stack.append(a + b)
            elif each =="-":
                stack.append(b-a)
            elif each == "*":
                stack.append( b * a)
            else:
                division = b/a
                if division < 0:
                    stack.append(ceil(division))
                else:
                    stack.append(int(division))
        else:
            stack.append(each)
            
    return stack[0]
    
    
print(calculate_exp(tokens1))
print(calculate_exp(tokens2))