"""
1877. Minimize Maximum Pair Sum in Array

"""
from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        c=len(nums)-1
        for i in range(len(nums)//2):
            ans=max(ans,nums[i]+nums[c])
            c-=1
        return ans
            
 
    
               
          
        # return maximum_output
   
    









answer = Solution().minPairSum([3,5,2,3,1])
print(answer)