spaces = 4
while True:
    try: 
        h = int(input("hight: "))
        w = int(input("width: "))
        break;
    except ValueError:
        print("hight and width have to be NUMBERS")

L = list()
for i in range (h*2 + 1):
    for j in range (w*spaces +1):
        if(i%2 == 0):
            if(j%spaces == 0):
                L+=("+")
               
            else:
                L+=("-")
        else:
            if(j%spaces == 0):
                L+=("|")
            else:
                L+=(" ")
        if(j == w*spaces):
            L+=("\n")

S = "".join(L)
print(S)
