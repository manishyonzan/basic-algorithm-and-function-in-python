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
    print("there is enemies is remaining and batte is not over")
else:
    print("enemy has 0 health and battle is over")




# the any will take a array and return true, if the array has atleast one truthy value in there
if any([False]):
    print("There is truthy value in the array")
else:
    print("there is no truthy value in there")
    