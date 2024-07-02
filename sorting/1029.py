"""
1029. Two City Scheduling

"""

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2  # Number of people to send to each city
        total_cost = 0
        
        # Sort the costs based on the difference between aCost and bCost
        costs.sort(key=lambda x: x[0] - x[1])
        print(costs)
        # Send the first n people to city A and the rest to city B
        for i in range(n):
            total_cost += costs[i][0]  # Send to city A
        for i in range(n, 2 * n):
            total_cost += costs[i][1]  # Send to city B
            
        return total_cost
      
                
            
    
answer = Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
print(answer)