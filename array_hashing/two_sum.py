"""
Two sum - 1

"""
from typing import List 

class Solution:
    def two_sum(self , nums:List[int] , target:int) -> List[int]:
        hashmap ={}
        for index  , n in enumerate(nums):
            b = target - n
            if b in hashmap:
                return [index , hashmap[b]]
            else:
                hashmap[n] = index
            print(hashmap)   


solution = Solution()
answer = solution.two_sum([2,1,5,3] , 4)
print(answer)

