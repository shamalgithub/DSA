from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        integer = str(int("".join(digits))+1)
        return [int(i) for i in integer]
        
        
        
       





print(Solution().plusOne([1,2,3]))