from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        hashmap = {index : i for index , i in enumerate(nums)}
        ranges = [keys for keys , values  in hashmap.items() if values == target]
        if len(ranges) > 1 :
            return [min(ranges) , max(ranges)]
        elif len(ranges) == 1:
            return [ranges[0] , ranges[0]]
        else:
            return [-1,-1]
        


print(Solution().searchRange([1] , 1))