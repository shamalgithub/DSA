"""
378. Kth Smallest Element in a Sorted Matrix

"""

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        flattened_list = [num for row in matrix for num in row]
        flattened_list.sort()
        if k <= len(flattened_list):
            return flattened_list[k-1]
        else:
            return flattened_list[-1]
       
      

answer = Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]] , 9)
print(answer)

