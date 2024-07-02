def simplestSum(k, a, b):
    
    sum = 0 
    for i in range(a , b+1):
        sum += i
        i *= k 
    
    print(sum%(10**7 + 7))
    


simplestSum(2 , 1 , 5)



