class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        reversed_number = number[::-1]
        if number == reversed_number:
            return True
        else:
            return False


print(Solution().isPalindrome(12))