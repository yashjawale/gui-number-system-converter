num = input("Enter a number: ")
frombase = int(input("Enter original base: "))
tobase = int(input("Enter desired base: "))

# print(num, "From ", frombase, "To", tobase)

def convert(num, frombase, tobase):
    decnum = int(num, frombase)
    
    if(tobase == 2):
        print(bin(decnum)[2:])
    
    if(tobase == 8):
        print(bin(decnum)[2:])
    
    if(tobase == 10):
        print(decnum)
    
    if(tobase == 16):
        print(hex(decnum)[2:]) 

convert(num, frombase, tobase)