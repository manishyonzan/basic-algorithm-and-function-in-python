# given string of the characters determine if all the characters are unique
# uppercase and lowercase should be considered different


def checkUnique(character):
    char_dict = {}
    for each in character:
        if each in char_dict:
            char_dict[each] = char_dict[each] + 1
        else:
            char_dict[each] = 1
    is_unique = True
    for key,elem in char_dict.items():
        if elem>1:
            is_unique=False
    return is_unique

print(checkUnique("staMm"))
