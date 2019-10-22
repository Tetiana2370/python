# Zadanie 1 
# 1. średników się nie używa, jeden z poprawnych sposobów
# x, y = 2, 3
# if (x > y):
#     result = x
# else:
#     result = y

# 2. po dwukropku nowa linia i tabulacja 
# for i in "qwerty": 
#     if ord(i) < 100: 
#         print (i)

# 3. dwukropki, tabulacje + akcja po warunku, a nie przed
# for i in "axby": 
#     if ord(i) < 100:
#         print ord(i) 
#     else:
#         i


# Zadanie 2
# 1. metoda sort() nie zwraca nic, funkcja sort() modykifuje obiekt, 
#    na który została wywołana
# 2. więcej wartości niż zmiennych, którym one są przypisywane
# 3. krotki nie mogą zostać zmodyfikowane
# 4. index (3) jest spoza zakresu 0-2
# 5. typ string nie posiada funkcji append()
# 6. funkcja pow musi przyjmować 2 argumenty, a nie jeden

# Zadanie 3
print("\tZadanie 3")

for i in range(30):
    if((i%3)!= 0):
        print(i)


# Zadanie 4
while True:
    x = input("x: ")
    if(x == "stop"):
        break
    try:
        print("%d, %d" %(int(x), int(x) ** 3))
    except ValueError:
        print("x has to be a number")
        

        
