DICTIONARY = {"I": 1, "V" : 5, "X":10, "C": 100, "D": 500, "M": 1000}

def check_roman(number):
    S = dict()
    prev = ""
    for i in list(number):
        if(i in S):
            if(i != prev or S[i] >= 3):
                return False
            S[i]+=1
        else:
            S.update({i: 1})
        prev = i
    return True
    
def roman2int(number):
    count = 1
    sum = 0
    prev = 0
    if check_roman(number) == False:
        print("FormatError in roman number: ", end=" ")
        return -1
    for i in list(number):
        try:
            if(DICTIONARY[i] == prev):
                count += 1
            elif(DICTIONARY[i] > prev):
                sum -= prev*count*2
                count = 1
            sum += DICTIONARY[i]
            if(DICTIONARY[i] != prev):
                count = 1
        except KeyError:
            print("KeyError in roman number: ", end="")
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
print(roman2int("XXXIV"))
print(roman2int("XXXXIIIV"))



