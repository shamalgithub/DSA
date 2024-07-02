"""
347. Top K Frequent Elements

"""
from typing import List
from collections import Counter
class Solution:
    def top_k_frequent(self , nums:List[int] , k:int) -> List[int]:
        counter = Counter(nums)
        hashmap = {}
        for n in nums:
            count = counter[n]
            if  n not in  hashmap:
                hashmap[n] = count
            
        print(hashmap)
        sorted_keys = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)
        print(sorted_keys)
        top_k_keys = sorted_keys[:k]
        return top_k_keys

solution = Solution()
answer = solution.top_k_frequent([1,1,1,2,2,2,3,3,3,3,3,3],  2)
print(answer)