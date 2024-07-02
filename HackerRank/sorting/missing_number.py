from collections import Counter

def missingNumbers(arr, brr):
    arr_counter = Counter(arr)
    brr_counter = Counter(brr)
    missing_list = []
    for key , value in brr_counter.items():
        if key in arr_counter:
            if value != arr_counter[key]:
                missing_list.append(key)
        else:
            missing_list.append(key)
    missing_list.sort()      
    return missing_list
                




print(missingNumbers([203 ,204 ,205 ,206 ,207 ,208 ,203 ,204 , 205 ,206], [203 ,204 ,204 ,205 ,206 ,207 ,205 ,208 ,203 ,206 ,205 ,206 ,204]))