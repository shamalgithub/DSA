class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashmap = {
            "I" : 1 ,
            "V" : 5 ,
            "X" : 10 ,
            "L" : 50 ,
            "C" : 100 ,
            "D" : 500 ,
            "M" : 1000 , 
        }
        number = 0
        for i in range(len(s)-1 , -1 , -1):
            if s[i] in hashmap:
                print(i)
                
                if i!=len(s)-1 and  s[i] == "I" and (s[i+1] =="V" or s[i+1] =="X"):
                    number -= hashmap[s[i]] 
                elif i!=len(s)-1 and s[i] == "X" and (s[i+1] =="L" or s[i+1] =="C"):
                    number -= hashmap[s[i]] 
                elif i!=len(s)-1 and s[i] == "C" and (s[i+1] =="D" or s[i+1] =="M"):
                    number -= hashmap[s[i]] 
                else:
                    number += hashmap[s[i]]
        
        return number
            



print(Solution().romanToInt("LVIII"))