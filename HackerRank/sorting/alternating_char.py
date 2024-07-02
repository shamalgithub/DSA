def alternatingCharacters(s):
    i =0 
    j = 1
    counter = 0 
    
    while i < len(s)-1:
        if s[i] == s[j]:
            counter+=1
        i+=1
        j+=1
    return counter
    


print(alternatingCharacters("AAAA"))