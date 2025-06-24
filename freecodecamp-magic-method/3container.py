# Container methods let you make your objects behave like built-in containers such as lists, dictionaries, or sets. 
# This is particularly useful when you need custom behavior for storing and retrieving data.



# Sequence Protocol
# To make your object behave like a sequence (like a list or tuple), 
# you need to implement these methods:

"""

Method	        Description	                                Example Usage
__len__	        Returns the length of the container	        len(obj)
__getitem__	    Allows indexing with obj[key]	            obj[0]
__setitem__	    Allows assignment with obj[key] = value	    obj[0] = 42
__delitem__	    Allows deletion with del obj[key]	        del obj[0]
__iter__	    Returns an iterator for the container	    for item in obj:
__contains__	Implements the in operator	                42 in obj

"""


# Mapping Protocol
# For dictionary-like behavior, you'll want to implement these methods:
"""

Method	        Description	                    Example Usage
__getitem__	    Get value by key	            obj["key"]
__setitem__	    Set value by key	            obj["key"] = value
__delitem__	    Delete key-value pair	        del obj["key"]
__len__	        Get number of key-value pairs	len(obj)
__iter__	    Iterate over keys	            for key in obj:
__contains__    Check if key exists	            "key" in obj


"""



# Practical Example: Custom Cache
# Let's implement a time-based cache that automatically expires old entries. 
# This example shows how to create a custom container that behaves like a dictionary but with additional functionality:


import time 
from collections import OrderedDict

class ExpiringCache:
    def __init__(self,max_age_seconds=60):
        self.max_age = max_age_seconds
        self._cache = OrderedDict()   # {key: (value, timestamp)}
        
    def __getitem__(self, key):
        if key not in self._cache:
            raise KeyError(key)
        value, timestamp = self._cache[key]
        
        if time.time() - timestamp > self.max_age:
            del self._cache[key]
            raise KeyError(f"Key '{key} has expired")
        
        return value
    
    
    def __setitem__(self, key, value):
        self._cache[key] = (value, time.time())
        self._cache.move_to_end(key)
    
    def __delitem__(self, key):
        del self._cache[key]
        
    def __len__(self):
        self._clean_expired()
        return len(self._cache)
    
    
    def __iter__(self):
        self._clean_expired()
        for key in self._cache:
            yield key
            
            
    def __contains__(self, key):
        if key not in self._cache:
            return False
        _, timestamp =  self._cache[key]
        
        if time.time() - timestamp > self.max_age:
            del self._cache[key]
            return False
        return True
    
    
    def _clean_expired(self):
        now = time.time()
        
        expired_keys = [
            key for key, (_,timestamp) in self._cache.items() if now - timestamp > self.max_age
        ]
        
        for key in expired_keys:
            del self._cache[key]
        
        
        
        
cache = ExpiringCache(max_age_seconds=2)

cache["name"] = "Vivek"
cache["age"] = 20

print("name" in cache)
print(cache["name"])    # Output: Vivek
print(len(cache))  

print("Waiting for expiration...")
time.sleep(3)

print("name" in cache) 

try:
    print(cache["name"])
except KeyError as e:
    print(f"keyerror : {e}")
    
print(len(cache))