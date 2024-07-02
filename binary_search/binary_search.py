
"""
Binary search algorithm O(log n )

"""



from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left_pointer = 0
        right_pointer = len(nums)-1
        while left_pointer <= right_pointer:
            midway_point = (right_pointer + left_pointer) // 2
            if nums[midway_point] == target:
                return midway_point
            elif nums[midway_point] < target :
                left_pointer = midway_point + 1
            else:
                right_pointer = midway_point -1 
        return -1  
        



solution = Solution()
answer = solution.search([-1,0,3,5,9,12] , 19)
print(answer)