import re
def pythonValidator(ipv4):
    failed = False
    eachAdresses = ipv4.split(".")
    print(eachAdresses)
    pattern = r'^0\d*'
    for each in eachAdresses:
        if not isinstance(int(each),int):
            failed = True
            print("break in not instance")
            break
        print(f"Pattern matching for {each}",bool(re.match(pattern, each)) )
        matched = bool(re.match(pattern, each))
        if matched or int(each)>256 or int(each)<0:
            failed = True
            break
    if failed:
        return "Not a ipv4"
    else:
        return "is a ipv4"
    
print(pythonValidator("192.168.1.1"))