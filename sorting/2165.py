"""
2165. Smallest Value of the Rearranged Number

"""




from typing import List


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            num_strings = [int(i) for i in str(num) if i!="0"]
            num_strings.sort()
            num_strings = [str(i) for i in num_strings]
            zero_strings = "".join([i for i in str(num) if i =="0"])
            end_string = "".join(num_strings[1:])
            output = int(num_strings[0]+zero_strings+end_string)
            return output
        else:
            num = num*(-1)
            num_strings = [int(i) for i in str(num)]
            num_strings.sort(reverse=True)
            num_strings = [str(i) for i in num_strings]
            output = "".join(num_strings)
            output = int(output) * -1
            return output
        
            
       


print(Solution().smallestNumber(-21008))






        
    