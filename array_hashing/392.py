class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 
        j = 0
        while i < len(s):
            if s[i] == t[j]:
                i+= 1
                j += 1
            elif j == len(t):
                return False
            else:
                j+= 1
            
        return True
                


print(Solution().isSubsequence("abc", "ahbgdc"))