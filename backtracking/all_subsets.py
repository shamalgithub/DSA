

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        i = 0

        while True:
            if i == len(nums):
                # Add a copy of the current subset to the result
                subset = [nums[j] for j in stack]
                res.append(subset)

                if not stack:
                    break
                
                i = stack.pop() + 1
            else:
                # Decision to include nums[i]
                stack.append(i)
                i += 1

        return res

# from collections import deque
# from typing import List

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         queue = deque()  # Use a queue for BFS
#         queue.append(([], 0))  # Start with an empty subset and the index 0

#         while queue:
#             subset, index = queue.popleft()  # Dequeue the current subset and index

#             # Add the current subset to the result
#             res.append(subset)

#             # Generate new subsets by including the next element
#             for i in range(index, len(nums)):
#                 new_subset = subset + [nums[i]]
#                 queue.append((new_subset, i + 1))  # Enqueue the new subset and next index

#         return res





print(Solution().subsets([0,1,2,3]))