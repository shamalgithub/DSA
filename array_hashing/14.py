from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        output_string = ""
        for index , i in enumerate(strs[0]):
            for j in range(1 , len(strs) , 1):
                if i == strs[j][index]:
                    continue
                else:
                    return output_string
            
            output_string = output_string+i
        
        return output_string
                
print(Solution().longestCommonPrefix(["ab", "a"]))