"""
229. Majority Element II

"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        condition = len(nums)//3
        
        hashmap = {}
        result_list = []
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] = hashmap[n]+1
        
        for key , value in hashmap.items():
            if value > condition:
                result_list.append(key)
        return result_list        
    
answer = Solution().majorityElement([1])
print(answer)