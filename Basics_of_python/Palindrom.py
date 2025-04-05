class Solution(object):
    @staticmethod
    def isPalindrome(x):
        if x < 0:
            return False
        reverse = 0
        xcopy = x
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        return reverse == xcopy

# Call the static method directly on the class
print(Solution.isPalindrome(121))  # True