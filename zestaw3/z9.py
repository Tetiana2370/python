L = [[],[4],(1,2),[3,4],(5,6,7)]
LS = list()
for i in L :
    tmp = 0
    for j in i:
       tmp += j 
    LS.append(tmp)
    
print(LS)
