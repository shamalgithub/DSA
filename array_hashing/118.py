
from typing import List 
from collections import deque

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangles = [[1]]
        for i in range(numRows-1):
            temp_deque = deque(pascal_triangles[i])
            temp_deque.append(0)
            temp_deque.appendleft(0)
            i = 0 
            j = i+1 
            temp_list = []
            while j < len(temp_deque):
                sum  = temp_deque[i] + temp_deque[j]
                temp_list.append(sum)
                i+=1
                j+=1
            pascal_triangles.append(temp_list)
        
        return pascal_triangles

            
            
            
        


print(Solution().generate(5))