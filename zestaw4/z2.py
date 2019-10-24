#zadanie 4.2.1

def get_ruler(x=5):
    if x<0:
        x*=-1
    
    L = list()

    for i in range(x*5+1):
        if(i%5 == 0):
          L.append("|")
        else:
          L.append(".")
    
    L.append("\n0")
    
    for i in range(1, x+1):
        L.append(str("%5s" % str(i)))
    return "".join(L)

print(get_ruler(-10))

#zadanie 4.2.2
import math

def get_mesh(h=3, w=3 ):
    spaces = 4
    if h<0 or w<0:
        h, w = abs(h) ,abs(w)
   
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

    return "".join(L)
    
print(get_mesh(3,3))
