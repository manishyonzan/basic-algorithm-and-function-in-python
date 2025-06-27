import time

class DirectClass:
    def __init__(self):
        self.value = 12
        
    
class GetAttrClass:
    def __init__(self):
        self._value= 12
    
    def __getattr__(self, name):
        if name == "value":
            return self._value
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


direct =  DirectClass()
getattr_obj = GetAttrClass()

def benchmark(obj,iterations=1000000):
    start = time.time()
    for _ in range(0,iterations):
        x = obj.value
    end = time.time()
    
    return end - start

direct_time = benchmark(direct)
getattr_time = benchmark(getattr_obj)

print(f"Direct access: {direct_time:.6f} seconds")
print(f"__getattr__ access: {getattr_time:.6f} seconds")
print(f"__getattr__ is {getattr_time / direct_time:.2f}x slower")



# 1. Be Consistent
# When implementing related magic methods, maintain consistency in behavior:

from functools import total_ordering

@total_ordering
class ConsistentNumber:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, ConsistentNumber):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, ConsistentNumber):
            return NotImplemented
        return self.value < other.value
    
    
# 2. Return NotImplemented
# When an operation doesn't make sense, return NotImplemented to let Python try the reverse operation:

class Money:
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        # ... rest of the implementation
        
        
# 3. Keep It Simple
# Magic methods should be simple and predictable. Avoid complex logic that could lead to unexpected behavior:

# Good: Simple and predictable
class SimpleContainer:
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

# Bad: Complex and potentially confusing
class ComplexContainer:
    def __init__(self):
        self.items = []
        self.access_count = 0

    def __getitem__(self, index):
        self.access_count += 1
        if self.access_count > 100:
            raise RuntimeError("Too many accesses")
        return self.items[index]
    
    
# 4. Document Behavior
# Clearly document how your magic methods behave, especially if they deviate from standard expectations:

class CustomDict(dict):
    def __missing__(self, key):
        """
        Called when a key is not found in the dictionary.
        Creates a new list for the key and returns it.
        This allows for automatic list creation when accessing
        non-existent keys.
        """
        self[key] = []
        return self[key]
    
    
# 5. Consider Performance
# Be aware of the performance implications, especially for frequently called methods:

class OptimizedContainer:
    __slots__ = ['items']  # Use __slots__ for better performance

    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]  # Direct access is faster
    
    
# 6. Handle Edge Cases
# Always consider edge cases and handle them appropriately:

class SafeContainer:
    def __getitem__(self, key):
        if not isinstance(key, (int, slice)):
            raise TypeError("Index must be integer or slice")
        if key < 0:
            raise ValueError("Index cannot be negative")
        # ... rest of the implementation
        
        
    