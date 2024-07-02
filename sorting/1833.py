from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        p =0
        total = 0 
        counter = 0
        while p<len(costs):
            total = total + costs[p]
            if total <= coins:
                counter +=1
            p +=1
        
        
        return counter

answer = Solution().maxIceCream( [1,3,2,4,1],  7)
print(answer)