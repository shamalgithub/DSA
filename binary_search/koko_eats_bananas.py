"""
SUPER IMPORTANT QUESTION - We dont have to maintain 
a separte list for k !! 

"""



from typing import List
import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # we could do this by adding the remainder to the next pile 
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
  
            
            
                
        
    
    
        

solution = Solution()
answer = solution.minEatingSpeed([3,6,7,11], 10)
print(answer)