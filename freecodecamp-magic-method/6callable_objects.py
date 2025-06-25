# Callable Objects
# The __call__ magic method lets you make instances of your class behave like functions. 
# This is useful for creating objects that maintain state between calls or for implementing function-like behavior with additional features.




# call
# The __call__ method is called when you try to call an instance of your class as if it were a function. Here's a simple example:

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        
    def __call__(self, x):
        return x * self.factor
    
# Create instances that behave like functions
double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Outpur: 15

# Practical Example: Memoization Decorator
# Let's implement a memoization decorator using __call__. 
# This decorator will cache function results to avoid redundant computations:


import time
import functools



class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        # Preserve function metadata (name, docstring, etc.)
        functools.update_wrapper(self, func)
        
    def __call__(self, *args, **kwargs):
        # Create a key from the arguments
        # For simplicity, we assume all arguments are hashable
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in self.cache:
            self.cache[key] = self.func(*args,**kwargs)
            
        return self.cache[key]
 
 
 
   
#usage
@Memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n -2)


#measure time
def time_execution(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__}({args}, {kwargs}) took {end - start:.6f} seconds")
    
    return result


# Without memoization, this would be extremely slow
print("Calculating fibonacci(35)...")
result = time_execution(fibonacci, 35)
print(f"Result: {result}")

# Second call is instant due to memoization
print("\nCalculating fibonacci(35) again...")
result = time_execution(fibonacci, 35)
print(f"Result: {result}")
    