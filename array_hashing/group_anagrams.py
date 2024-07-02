"""
Group anagrams - 49
"""
from typing import List

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in hashmap:
                hashmap[s_sorted] = [s]
            else:
                hashmap[s_sorted].append(s)
        return list(hashmap.values())

solution = Solution()
answer = solution.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(answer)

        
        