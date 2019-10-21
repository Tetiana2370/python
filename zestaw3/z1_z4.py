# Zadanie 1 
# 1. ok
# 2. po dwukropku i spacja(o jedną wiecej niż w linijce z warunkiem
# 3. po warunku if i else - dwukropek, po dwukropkach nowa linia + tabulacja.

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
        

        
