from typing import List 

# the recursion is correct the logic is wrong for n-1 instance can correct for n 
def findmax(array:List , i:int)->int:
    j = len(array)- i -1
    print("j" , j , "i" , i)
    
    if j == 1:
        return array[j]
    elif j == 0:
        return array[j]
    else:
        right = array[j]
        i += 2
        return findmax(array=array , i=i) + right 

# print((findmax(array=[2,7,9,3,1], i=0) , findmax(array=[2,7,9,3,1] , i=1)))
print(findmax(array=[2 , 7, 9, 3,1] , i =0))