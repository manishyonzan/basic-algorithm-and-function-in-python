chars = ["a","b", "c", "d", "e"]
result = ""
for char in chars:
    result += char
# this is o(n^2) complexity because string create a new string when it is traversed and appended

# so we should do :
result = []
for char in chars:
    result.append(char)
"".join(result)
# for o(n)