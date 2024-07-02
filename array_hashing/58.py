class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s_split = s.split()
        last_string_lenght = len(s_split[len(s_split)-1])
        return last_string_lenght
        
       


print(Solution().lengthOfLastWord("luffy is still joyboy"))