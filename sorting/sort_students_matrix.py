"""
2545. Sort the Students by Their Kth Score

"""
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        hashmap = {}
        for index , i in enumerate(score):
            hashmap[index] = i[k]
        
        sorted_index = sorted(hashmap.keys() , key=lambda x : hashmap[x]  , reverse=True)
        sorted_matrix = []
        for m in sorted_index:
            sorted_matrix.append(score[m])
        return sorted_matrix
    
    
    
solution = Solution()

answer = solution.sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]],  2)

print(answer)