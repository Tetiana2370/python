#   Zakładam że nie zdarzy się sytuacji typu: IIIIV, VVX
DICTIONARY = {"I": 1, "V" : 5, "X":10, "C": 100, "D": 500, "M": 1000}

def roman2int(number):
    sum = 0
    prev = 1
    for i in list(number):
        try:
            if(DICTIONARY[i] > prev):
                sum = DICTIONARY[i] - sum;
            else: 
                sum+= DICTIONARY[i]
        except KeyError:
            print("value error in roman number")
            return -1
        prev = DICTIONARY[i]
    return sum

print(roman2int("VIII"))
print(roman2int("MVIII"))
print(roman2int("IIV"))
print(roman2int("IX"))
print(roman2int("XI"))
print(roman2int("HIII"))
print(roman2int("CM"))

