"""
2587. Rearrange Array to Maximize Prefix Score

"""
from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        score_counter = 0
        score =0
        for index  , i in enumerate(nums):
            score += nums[index] 
            if score > 0 :
                score_counter +=1
        return score_counter
    
answer = Solution().maxScore([-2,-3,0])
print(answer)