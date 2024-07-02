
def icecreamParlor(m, arr):
    i=0
    j = 1
    
    while i < len(arr):
        if arr[i] + arr[j] == m:
            return sorted([i+1 , j+1])
        elif j == len(arr)-1:
            i+=1
            j = i + 1
        else:
            j+=1
    


print(icecreamParlor(6 , [1,3,4,5,6]))