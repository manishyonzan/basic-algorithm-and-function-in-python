# binary to decimal
# start by multiplying right most by 2^0  and the next by 2^1 and so on and in the end add them


def toDecimal(binary:str):
    sum = 0
    for index,item in enumerate(binary[::-1]):
        if item not in "10":
            print("only binary is allowed")
            return None
        sum += int(item) * 2**index 
    return sum
    
print(toDecimal("101"))
print(toDecimal("1101"))



# To convert a decimal number to binary, you repeatedly divide the number by 2 and record the remainder at each step.

def decimal_to_binary(decimal:int):
    binary = ""
    if decimal == "0":
        return 0
    while decimal>0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal//2
    return binary

print(decimal_to_binary(5))
print(decimal_to_binary(13))
        