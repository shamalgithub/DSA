"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

"""
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        set_check = set(nums)
        if len(set_check) == 1:
            return len(nums)
        
        
        
        sub_seq_length = 1
        l = 0
        r = 1
        
        while l < r and r < len(nums):
            difference  = abs(max(nums[l:r+1]) - min(nums[l:r+1]))
            print(difference)
            if difference <= limit:
                sub_seq_length = max(sub_seq_length , len(nums[l:r+1]))
                r+=1
            else:
                l += 1
                r += 1
           
        return sub_seq_length

   

answer = Solution().longestSubarray(  [8,2,4,7], 4)
print("subsequence" , answer)
                
            


       
            