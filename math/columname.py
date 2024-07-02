"""
daily challenge -  168. Excel Sheet Column Title
 

"""

# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         alphabet_positions = {(letter - ord('a') + 1 ): (chr(letter)).upper() for letter in range(ord('a'), ord('z') + 1)}

#         if columnNumber <= 26 : 
#             return alphabet_positions[columnNumber]
#         column_name = ""
#         while columnNumber > 0:
#             quotient, remainder = divmod(columnNumber - 1, 26)
#             column_name = alphabet_positions[remainder + 1] + column_name
#             columnNumber = quotient
#         return column_name
                    
class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while(n > 0):
            n -= 1
            curr = n % 26
            n = int(n / 26)
            ans.append(chr(curr + ord('A')))
        
        return ''.join(ans[::-1])                  
                    

solution = Solution()
answer = solution.convertToTitle(2147483647)
print(answer)