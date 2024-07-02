def makingAnagrams(s1, s2):
    h1 = {}
    h2 = {}
    set_string = set(s1+s2)
    removed_count =  0
    for s in s1:
        if s in h1:
            h1[s]+=1
        else:
            h1[s] = 1
    for s in s2:
        if s in h2:
            h2[s] +=1
        else:
            h2[s] = 1
    
    for s in set_string:
        if s in h1 and s in h2:
            if h1[s] != h2[s]:
                removed_count += abs(h1[s] - h2[s])
        else:
            if s in h1:
                removed_count += h1[s]
            else:
                removed_count += h2[s]
    
    return removed_count
        




print(makingAnagrams("abc" , "aaabc"))