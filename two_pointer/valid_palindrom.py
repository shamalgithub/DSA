"""
valid palindrom 
"""

class Solution:
    def is_plaindrom(self , s:str) -> bool:
        s = s.lower()
        print(s)
        cleaned_string = ""
        for char in s:
            if char.isalnum():
                cleaned_string += char
        
        print(cleaned_string)
        reversed_string = cleaned_string[::-1]
        print(reversed_string)
        if reversed_string == cleaned_string:
            return True
        else:
            return False

solution = Solution()
answer = solution.is_plaindrom("A man, a plan, a canal: Panama")
print(answer)