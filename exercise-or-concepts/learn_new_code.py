# lets see how to use the any function

enemies = [
    {
        "type":"Orc",
        'health':5
    },
    {
        "type":"Orc",
        'health':0
    },
    {
        "type":"Orc",
        'health':1
    },
    {
        "type":"Orc",
        'health':1
    },
]

if any([enemy["health"] for enemy in enemies]):
    print("There is enemies is remaining and batte is not over")
else:
    print("Enemy has 0 health and battle is over")



# lets change the health to 0
enemies = [
    {
        "type":"Orc",
        'health':0
    },
    {
        "type":"Orc",
        'health':0
    },
    {
        "type":"Orc",
        'health':0
    },
    {
        "type":"Orc",
        'health':0
    },
]

if any([enemy["health"] for enemy in enemies]):
    print("There is enemies is remaining and batte is not over")
else:
    print("Enemy has 0 health and battle is over")




# the any will take iterable and return true, if the it has atleast one truthy value in there
if any([False]):
    print("There is truthy value in the array")
else:
    print("There is no truthy value in there")
    
    
    
    
"""                                mutable args and ummutable args                                                      """

def mutable(arg):
    """ Highlights that list, set and dict types are mutable """
    if isinstance(arg,list):
        arg.append("Your list was modified by mutable function")
    if isinstance(arg,set):
        arg.add("Your set was modified by mutable function")
    if isinstance(arg,dict):
        arg["added"] = "Your list was modified by mutable function"

def immutable(arg):
    if isinstance(arg, float) or isinstance(arg, int):
        arg+=1
    if isinstance(arg,str):
        arg+="this will not affect your str"

def check_mutable_immutable():
    # in python list, set and dict are mutable
    for item in [[1,2], {2,3}, {"key":"value"}]:
        mutable(item)
        print(item)    
        
    for item in [0.0, 1, 'just a string']:
        immutable(item)
        print(item)
        
print("mutable and immutable")
check_mutable_immutable()