from functools import lru_cache

@lru_cache(maxsize=None)
def climb(n:int) -> int:
    counter = 0 
    if n ==0 or n==1 :
        counter += 1 
        return 1
    else:
        return climb(n-1) + climb(n-2)
    

print(climb(200))