import pandas


class System:
    def __init__(self, num, old_base, new_base):
        self.num = num
        self.old_base = old_base
        self.new_base = new_base

    def actual_num(self):
        num1 = int(self.num, self.old_base)
        return num1

    def covert_num(self):
        if self.new_base == 2:
            return bin(self.actual_num())

        elif self.new_base == 8:
            return oct(self.actual_num())

        elif self.new_base == 16:
            return hex(self.actual_num())

        elif self.new_base == 10:
            return self.num

        else:
            return "Only hex, oct , bin , dec conv possible"


dict1 = {"Num": ["Binary", "Hexadecimal", "Octal", "Decimal"], "Base": [2, 16, 8, 10]}
df = pandas.DataFrame(dict1)
print(df)

number = input("Enter a number: ")
old1base = int(input("Enter its base: "))
new1base = int(input("Enter base of sys in which you want to convert the num: "))
num_sys = System(number, old1base, new1base)

print(num_sys.covert_num())
