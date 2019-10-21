L = list()
try: 
    x = int(input("length : "))
    if int(x) < 0:
        x *= -1
        
except ValueError:
    print("You had 1 chance...length will be 12")
    x = 12

for i in range(x*5+1):
    if(i%5 == 0):
       L.append("|")
    else:
       L.append(".")

L.append("\n0")

for i in range(1, x+1):
    L.append(str("%5s" % str(i)))
L = "".join(L)
print(L)
