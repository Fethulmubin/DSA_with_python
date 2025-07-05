# https://leetcode.com/problems/search-a-2d-matrix/
class Solution(object):
    def search(self, nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if target < nums[mid]:
                R = mid - 1
            elif target > nums[mid]:
                L = mid + 1
            else:
                return mid
        return -1
                    
# Example usage:
sol = Solution()
print(sol.search([1, 2, 3, 4, 5], 3))
# Output: 2
# Explanation: The function performs a binary search on the sorted list nums to find the index of target.
# If target is found, it returns the index; otherwise, it returns -1.
# This code defines a class Solution with a method search that implements binary search on a sorted list.