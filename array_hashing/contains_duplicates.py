"""
contains duplicates - 217
"""
from typing import List

class Solution:
    def contains_duplicates(self , nums:List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True 
            else:
                hashset.add(n)
        return False 


solution = Solution()
answer = solution.contains_duplicates([1,2,4,5])
print(answer)