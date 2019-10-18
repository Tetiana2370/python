# Xadanie 2.9

# def copy_file(inputfile_name, outputfile_name):
#         input = open(inputfile_name, "r")
#         output = open(outputfile_name, "w")
#         temp=input.readline()
#         while True:
#             if not temp:
#                 break
#             index = temp.find("#")
#             if index == -1:
#                 index = len(temp)
#             output.write(temp[:index] + "\n")
#             temp=input.readline()

# Zadanie 2.10
print("\nZadanie 2.10")

line = """what a
wonderful weather
	     today"""
print(line)
print(len(line.split()))

# Zadanie 2.11
print("\nZadanie 2.11")

L = list("word");
word = "_".join(L)
print (word)

# Zadanie 2.12
print("\nZadanie 2.12")

S = "what a wonderful world"
print(" ".join([s[:1] for s in S.split()]))

# Zadanie 2.13
print("\nZadanie 2.3")

S = "what a wonderful world"
print(sum([len(x) for x in S.split()]))

# Zadanie 2.14 a)
print("\nZadanie 2.14 a)")
max = 0;
line = "What a wonderful world"
for i in list(line.split(" ")): 
    if len(i) > max:
        max = len(i);

print("max len is: %d" % max)

# Zadanie 2.14 b)
print("\nZadanie 2.14 b)")

max = ""
for i in list(line.split(" ")): 
    if len(i) > len(max):
        max = i;
print("the longest word is : %s" % max)

# Zadanie 2.15
print("\nZadanie 2.15")

L = [10, 4, 23, 2, 0, 3, 6, 2, 1]
line = "".join(str(L).split(", "))
print(line)


# Zadanie 2.16
print("\nZadanie 2.16")

line = "some words some words GvR some words"
L = list()
for i in list(line.split(" ")):
    if i=="GvR":
        print(i)
        L += "Guido van Rossum "
    else:
        L += i + " ";

print("".join(L))


# Zadanie 2.17
print("\nZadanie 2.17")

line = "car notebook array zipper lake professional frequency"

print(sorted(line.split(" ")))
print(sorted(line.split(" "), key = str.__len__))


# Zadanie 2.18
print("\nZadanie 2.18")

print(str(1040330002222450).count("0"))

# Zadanie 2.19
print("\nZadanie 2.19")

L = [1, 22, 333, 4, 5, 666, 7, 88, 999]
print(" ".join([ str(i).zfill(3) for i in L]))


