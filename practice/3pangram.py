# given a word or sentence and a string of lowercase letters , determine if the word or sentence uses all the
# letters from the given set once and no other letters

# ignore non alphabetical characters in the word or sentence
# ignore letter casing in the word or sentence


# def is_pangram(sentence, letters):
    
#     arr_of_required_letters = set(str.lower(letters))
#     arr_of_sentence_to_check = set(str.lower(sentence))
#     result = "Uses every alphabet of letter list"
    
#     for each in arr_of_sentence_to_check:
#         if each not in arr_of_required_letters and each.isalpha():
#             result = "Do not use every letter in the list"
#             break
#     return result


def is_pangram(sentence, letters):
    # Normalize both inputs: lowercase and filter only alphabetic characters
    normalized_sentence = set(ch.lower() for ch in sentence if ch.isalpha())
    normalized_letters = set(letters.lower())

    # Check if all required letters are present in the sentence
    if normalized_letters.issubset(normalized_sentence):
        return "Uses every letter in the list at least once"
    else:
        return "Does not use every letter in the list"

print(is_pangram("e lll", "ell"))
            


    
    