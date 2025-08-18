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




# the any will take a array and return true, if the array has atleast one truthy value in there
if any([False]):
    print("There is truthy value in the array")
else:
    print("There is no truthy value in there")
    