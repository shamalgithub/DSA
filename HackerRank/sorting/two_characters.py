from collections import Counter 


def alternate(s):
    counter = Counter(s)
    hashmap  = {element : count for element , count in counter.items() if count >= 2}
    string_set  = list(hashmap.keys())
    print(string_set)
    i = 0 
    j = i+1
    while i < len(string_set)-1:
        print(i , j)
        substring = "".join([k for k in s if k == string_set[i] or k==string_set[j]])
        if substring :
            return len(substring)
        elif j == len(string_set)-1:
            i +=1
            j = i+1
        else:
            j+=1
            



print(alternate("abadabdc"))