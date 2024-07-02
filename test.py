from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        hashmap  = {}
        
        for i in range(m):
            for j in range(n):
                if i - j not in hashmap:
                    hashmap[i - j] = []  
                hashmap[i - j].append(matrix[i][j])
        print(hashmap)       
        for k in hashmap:
            hashmap[k].sort(reverse=True) 
        
        print(hashmap)   
        for i in range(m):
            for j in range(n):
                matrix[i][j] = hashmap[i - j].pop()   
                
      



answer = Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])






