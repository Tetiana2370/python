import functools
def factorial(n):
    if n < 0:
        print("ERROR: n < 0")
        return -1
      
    elif(n==0 or n==1):
        return 1
    return functools.reduce(lambda x, y: x*y, list(range(1,n+1)))



#or

# def factorial(n):
#     if n < 0:
#         print("ERROR: n < 0")
#         return -1
      
#     elif(n==0 or n==1):
#         return 1
#     tmp = 1;
#     for i in range(1,n+1):
#         tmp*=i;
#     return tmp;
