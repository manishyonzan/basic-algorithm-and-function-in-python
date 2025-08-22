# this is not from the w3 schools


x = "102"
a = x.find("0")
print(a)  # Output: 1

# str.find() returns the lowest index of the substring if found, or -1 if not found.


x = [1, 0, 2]
a = x.index(0)
print(a)  # Output: 1

# if not in the list
try:
    x = [1,2,3]
    a= x.index(0)
    print("the index of 0 is ",a)
except ValueError as v:
    print(v)
    

def find_in_list(lst, value):
    return lst.index(value) if value in lst else -1

x = [1, 0, 2]
a = find_in_list(x, 0)
print(a)  # Output: 1

data = [
    {"id": 1, "name": "Manish"},
    {"id": 2, "name": "Aarav"},
    {"id": 2, "name": "haribahadur"},
    {"id": 3, "name": "Sita"}
]

# Find the dictionary with id == 2
result = next((item for item in data if item["id"] == 2), None)
print(result)  # Output: {'id': 2, 'name': 'Aarav'}

matches = [item for item in data if item.get("id") == 2]
print(matches)




def find_dicts_by_keys(data, **criteria):
    """
    Returns all dictionaries in the list that match all key-value pairs in criteria.
    
    Parameters:
        data (list): List of dictionaries.
        **criteria: Arbitrary keyword arguments representing key-value filters.
    
    Returns:
        list: Matching dictionaries.
    """
    return [
        item for item in data
        if all(item.get(k) == v for k, v in criteria.items())
    ]
    
# If you ever want to check if at least one condition is true inside of the  bracket of all( it will return true if [True,True] else false), use any() instead:    
# all(item.get(k) == v for k, v in criteria.items())
# If you ever want to check if at least one condition is true inside of the  bracket of any(here) any will return true if atleast one is true like [true, false], use any() instead:
# any(item.get(k) == v for k, v in criteria.items())

    
users = [
    {"id": 1, "name": "Manish", "role": "admin"},
    {"id": 2, "name": "Aarav", "role": "user"},
    {"id": 3, "name": "Sita", "role": "admin"},
    {"id": 4, "name": "Manish", "role": "user"}
]

# Find all users with name "Manish"
print(find_dicts_by_keys(users, name="Manish"))

# Find all admins named "Sita"
print(find_dicts_by_keys(users, name="Sita", role="admin"))



# if you just want first match 

def find_first_dict_by_keys(data, **criteria):
    return next(
        (item for item in data if all(item.get(k) == v for k, v in criteria.items())),
        None
    )