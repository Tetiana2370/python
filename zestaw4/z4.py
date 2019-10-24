def fibonacci(n):
    x1, x2 = 0, 1
    if(n < 0):
        print("ERROR: n < 0")
        return -1
    if (n == 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    for i in range(2, n+1):
        tmp = x2
        x2 = x2+x1
        x1 = tmp
    return x2
