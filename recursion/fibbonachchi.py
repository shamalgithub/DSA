
class Solution:
    def fibbonachchi(self , n:int)->int:
        #base case 
        if n == 1 or n == 2:
            return 1
        else:
            return self.fibbonachchi(n-1) + self.fibbonachchi(n-2)

solution = Solution()
fibbonachi = solution.fibbonachchi(70)
print(fibbonachi)

# class Solution:
#     def __init__(self):
#         self.memo = {}

#     def fibonacci(self, n: int) -> int:
#         if n in self.memo:
#             return self.memo[n]

#         if n == 1 or n == 2:
#             return 1
#         else:
#             result = self.fibonacci(n - 1) + self.fibonacci(n - 2)
#             self.memo[n] = result
#             return result

# solution = Solution()
# fibonacci_100 = solution.fibonacci(100)
# print(fibonacci_100)
