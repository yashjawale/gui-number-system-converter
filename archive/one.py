# num = input("Enter a number: ")
# frombase = int(input("Enter original base: "))
# tobase = int(input("Enter desired base: "))

# print(num, "From ", frombase, "To", tobase)


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


# print(convert(num, frombase, tobase))