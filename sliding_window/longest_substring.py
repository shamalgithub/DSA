
"""
longest substring - important 

"""

class Solution:
    def longest_substring(self , s:str) -> int:
        hashset = set()
        l , r = 0 , 1 
        max_substring = 0
        hashset.add(s[l])
        while r<= len(s)-1:
            if s[r] in hashset:
                l = r
                r += 1
            else:
                max_substring = max(max_substring , (r-l+1))
                hashset.add(s[r])
                r += 1
        return max_substring
    

solution = Solution()
answer = solution.longest_substring("pwwkew")
print(answer)
           
                