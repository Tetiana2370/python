# iteracyjnie

def reverse(L, left, right):
    if(left==right or right==0 or left > len(L) or right > len(L)):
        return None
    new_list = L[:left]
    for i in range(right-left + 1 ):
        new_list.append(L[right - i] )
    new_list.extend(L[right+1:])
    return new_list     
    
# rekurencyjnie
# def reverse(L, left, right):
#     if left+1 != right and left != right:
#         L[left], L[right] = L[right], L[left]
#         return reverse(L, left+1, right-1)
#     if left+1 == right:
#          L[left], L[right] = L[right], L[left]
#     return L

LL = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
print(reverse(LL, 0, 9))
print(reverse(LL, 3, 6))
