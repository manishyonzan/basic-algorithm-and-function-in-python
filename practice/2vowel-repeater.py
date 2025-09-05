# giver a string repeat a new version of the string where each vowel is duplicated one more time than the previoius encountered

def repeat_vowels(s):
    string_array = list(s)
    vowel_letters = ["a", "e", "i", "o", "u"]
    repeat_times = 0
    new_String = []
    for alph in string_array:
        string_to_push = ""
        if str.lower(alph) in vowel_letters:
            string_to_push = alph + str.lower(alph)*repeat_times
            repeat_times+=1
        else:
            string_to_push = alph
        new_String.append(string_to_push)
    return "".join(new_String)
            
            
            
            
    
print(repeat_vowels("alphaeEPO u"))   