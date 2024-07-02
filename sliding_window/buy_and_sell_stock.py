"""
important - was able to solve 
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        profit = 0
        while r <= len(prices)-1:
            if prices[l] < prices[r]:
                buy = prices[l]
                spot_profit = prices[r] - prices[l]
                profit = max(profit , spot_profit)
                r +=1
            else:
                l = r
                r +=1
        return profit
            

            

solution = Solution()
answer = solution.maxProfit([2,2,1,5,3,2])
print(answer)