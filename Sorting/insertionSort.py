class Solution(object):
    def sortArray(self, nums):
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j + 1] < nums[j]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp
                j -= 1
        return nums
    # sorting with insertion sort
    # time complexity: O(n^2)
    # space complexity: O(1)
    # stable sort
    # in-place sort
    # best case: O(n) when the array is already sorted
    # worst case: O(n^2) when the array is sorted in reverse order
    # average case: O(n^2)