from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def area_calculation(left , right):
            area_value = min(height[left] , height[right])*(right - left)
            return area_value
        
        left_pointer  = 0
        right_pointer = len(height)-1
        area = 0
        while left_pointer < right_pointer:
            area = max( area , area_calculation(left_pointer , right_pointer))
            if height[left_pointer] > height[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
        return area

solution = Solution()
answer = solution.maxArea([1,8,6,2,5,4,8,3,7])
print(answer)