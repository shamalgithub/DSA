from collections import Counter


def gameOfThrones(s):
    counter = Counter(s)
    hashmap  = {element : count for element , count in counter.items()}
    print(hashmap)
    odd_counter  = 0 
    for i in hashmap.keys():
        if hashmap[i] % 2 != 0 :
            odd_counter +=1
    
    if odd_counter == 1 or odd_counter == 0 :
        return "YES"
    else:
        return "NO"


print(gameOfThrones("ababcccb"))