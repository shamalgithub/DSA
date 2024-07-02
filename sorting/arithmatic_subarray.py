"""
1630 - arithmatic sub array 

"""

from typing import List 

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for L , R in zip(l,r):
            a = False
            subarray = sorted(nums[L:R+1])
            difference = subarray[1] - subarray[0]
            s =0
            while s < len(subarray)-1:
                if subarray[s+1]-subarray[s] == difference:
                    a = True
                    s +=1 
                else:
                    a = False
                    break
            answer.append(a)
        return answer
                
                    
                    

            
            


solution = Solution()
answer = solution.checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10])
print(answer)