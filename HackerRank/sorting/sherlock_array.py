def balancedSums(arr):
    
    i = 0 
    for i in range(len(arr)):
        if i == 0 :
            if sum(arr[i+1:len(arr)]) == 0:
                return "YES"
            else:
                i+=1
        elif sum(arr[0:i]) == sum(arr[i+1:len(arr)]):
            return "YES"
 
    return "NO"






print("return value -->",balancedSums([1, 1 ,4 ,1, 1]))