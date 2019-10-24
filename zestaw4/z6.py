def sum_seq(sequence):
    result = 0
    for i in sequence:
        if(isinstance(i, (list, tuple))):
            result+=sum_seq(i)
        else:
            result+=i;
    
    return result

print(sum_seq([(1, 2), 3, [4, 5]]))
