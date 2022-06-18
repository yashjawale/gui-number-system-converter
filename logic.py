def getbase(string):
    if(string == "Binary"):
        return 2
    elif(string == "Octal"):
        return 8
    elif(string == "Decimal"):
        return 10
    else:
        return 16

def convert(num, frombase, tobase):
    decnum = int(num, frombase)
    if tobase == 2:
        return bin(decnum)[2:]
    if tobase == 8:
        return bin(decnum)[2:]
    if tobase == 10:
        return decnum
    if tobase == 16:
        return hex(decnum)[2:]