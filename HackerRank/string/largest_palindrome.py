
def highestValuePalindrome(s, n, k):
    l , r = 0 , n-1
    number_of_swaps = 0
    largest_palindrome = ""
    if k == n:
        largest_palindrome = "".join(["9" for i in s])
        number_of_swaps = n
        return largest_palindrome
    if k > 2 : 
        s = "9" + s[1:len(s)-1] + "9"
        number_of_swaps += 2
        l +=1 
        r -= 1
    s = [i for i in s]

    while l < r : 
        if int(s[l]) > int(s[r]):
            s[r] = s[l]
            l += 1
            r -= 1
            number_of_swaps+=1
        elif int(s[l]) == int(s[r]):
            l+=1
            r-= 1
        else :
            s[l] = s[r]
            number_of_swaps += 1
        if number_of_swaps == k:
            break
    
    s = "".join(s)
    s_reversed = s[::-1]
    
    if s == s_reversed:
        return s
    else :
        return "-1"
        
        



print(highestValuePalindrome("932239" , 6 , 2))