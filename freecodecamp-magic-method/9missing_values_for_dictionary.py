# missing for Default Dictionary Values
# The __missing__ method is called by dictionary subclasses when a key is not found.
# This is useful for implementing dictionaries with default values or automatic key creation.

# Here's an example of a dictionary that automatically creates empty lists for missing keys:



class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key]=[]
        return self[key]
    
# Usage
groups = AutoKeyDict()
groups["team1"].append("Vivek")
groups["team1"].append("Wewake")
groups["team2"].append("Vibha")

print(groups)  # Output: {'team1': ['Vivek', 'Wewake'], 'team2': ['Vibha']}