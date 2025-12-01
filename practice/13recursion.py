def factorial(n):
    print(f"calculating factorial {n}")
    answer = None
    if n <=1:
        answer = 1
    else:
        answer = n * factorial(n-1)
    print(f"returning factorial of {n}, result = {answer}")
    return answer

print(factorial(5))