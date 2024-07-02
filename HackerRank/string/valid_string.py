from collections import Counter

def isValid(s):
    s_set = set(s)
    counter = Counter(s)
    hashmap  = {}
    for char , count in counter.items():
        hashmap[char]=count
    
    sorted_list_reverse  = sorted(hashmap.values() , reverse=True)
    sorted_list = sorted(hashmap.values())
    
    if len(set(sorted_list_reverse)) ==1:
        return "YES"
    else:
        sorted_list_reverse[0] = sorted_list_reverse[0]-1
        sorted_set = set(sorted_list_reverse)
        if len(sorted_set) ==1:
            return "YES"
        else:
            sorted_list.pop(0)
            if len(set(sorted_list)) == 1:
                return "YES"
            else:
                return "NO"
     
        


print(isValid("aabbcd"))