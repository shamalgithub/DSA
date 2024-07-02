"""
valid anagram - 242 
"""
class Solution:
    def is_anagram(self , s:str , t:str) -> bool :
        # see if the two strings are of equal length 
        if len(s) != len(t):
            return False
        else:
            s_sort = ''.join(sorted(s))
            t_sort = ''.join(sorted(t))
            if s_sort == t_sort:
                return True
            else:
                return False

solution = Solution()
answer = solution.is_anagram("anagram", "nagaram")
print(answer)