"""
Minimum window substring - AirBnB Hard question Could not solve - Try agian !! 

When we find a suitable substring we move the L and R to the next section 
"""

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         hashmap_t ={}
        
#         for char in t:
#             hashmap_t[char] = hashmap_t.get(char , 0)+1
        
#         l , r = 0 ,1 
#         minimum_window = len(s)
        
#         while r <= len(s)-1 :
            
#             # check if every character present in string t is in the substring 
            
            
