"""
238 - Product of Array Except Self - HARD

"""

from typing import List 

class Solution:
    def product_of_array(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


solution = Solution()
answer = solution.product_of_array([1,2,3,4,5])
print(answer)