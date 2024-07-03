from collections import Counter

def check_if_palindrome(string:str)->bool: 
    # sorted_string = sorted(string)
    character_count = Counter(string)
    hashmap = {}
    odd_counter = 0 
    for char , count in character_count.items():
        hashmap[char] = count 

    for i in hashmap.keys():
        if hashmap[i] % 2 != 0 :
            odd_counter +=1
    
    if odd_counter == 1 or odd_counter == 0 :
        return True
    else:
        return False


def highestValuePalindrome(s:str, n:int, k:int) ->str:
    s = list(s)
    changes_needed = [0] * (n // 2)
    print(changes_needed)
    
    # Count the minimum changes needed to make it a palindrome
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            changes_needed[i] = 1
    
    if sum(changes_needed) > k:
        return '-1'
    
    # Make the string a palindrome with minimum changes
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            max_digit = max(s[i], s[n - 1 - i])
            s[i] = s[n - 1 - i] = max_digit
            k -= 1
    
    # Use remaining changes to maximize the palindrome
    i = 0
    while k > 0 and i < n // 2:
        if s[i] != '9':
            if changes_needed[i] == 0 and k >= 2:
                s[i] = s[n - 1 - i] = '9'
                k -= 2
            elif changes_needed[i] == 1 and k >= 1:
                s[i] = s[n - 1 - i] = '9'
                k -= 1
        i += 1
    
    # If there's an odd number of digits and we have a change left, make the middle digit 9
    if k > 0 and n % 2 == 1:
        s[n // 2] = '9'
    
    return ''.join(s)





print(highestValuePalindrome("3943" , 4 , 1))