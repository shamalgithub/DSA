
from typing import List 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(nums , target):
            l , r = 0 , len(nums)-1
            while l <= r:
                mid_point  = (l + r)//2 
                if nums[mid_point] == target :
                    return mid_point
                else:
                    if nums[mid_point] < target : 
                        l = mid_point + 1
                    else :
                        r = mid_point - 1
            return - 1
        return_value = binary_search(nums , target)
        if return_value < 0 :
            nums.append(target)
            nums.sort()
            return binary_search(nums , target)
        else:
            return return_value
      
        



print(Solution().searchInsert([1,3] , 1) )