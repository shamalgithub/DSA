from functools import lru_cache


def superDigit(n, k):
    x = n*k 
    @lru_cache(maxsize=None)
    def digit(x:str)->str:
        if len(x) == 1:
            return x
        else:
            x = str(sum(int(i) for i in x))
            return digit(x)
    return digit(x=x)


print(superDigit(n="9875" , k=4))