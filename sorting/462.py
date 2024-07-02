"""
462. Minimum Moves to Equal Array Elements II

"""
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        moves_list = []
        s = 0
        f = len(nums) -1
        while s<len(nums):
            difference = abs(nums[f] - nums[s])
            moves += difference
            f -= 1
            if f < 0 : 
                f = len(nums)-1
                s += 1
                moves_list.append(moves)
                moves = 0 
        return min(moves_list)
    
answer = Solution().minMoves2([1,2,3])
print(answer)