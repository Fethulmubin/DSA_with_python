
# insertion sort implementation in Python
# insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time
# it is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort
# it is a stable sort, meaning that it maintains the relative order of records with equal keys
# it is an in-place sort, meaning that it requires only a constant amount of additional space
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
    
    
    
    # merge_sort implementation in Python
    class Solution(object):
        def sortArray(self, nums):
            self.mergeSort(nums, 0, len(nums) - 1)
            return nums
        def mergeSort(self, nums, start, end):
            if end - start + 1 <= 1:
                return
            middle = (end + start) // 2
            self.mergeSort(nums, start, middle)
            self.mergeSort(nums, middle + 1, end)
            self.merge(nums, start, middle, end)
        def merge(self, nums, start, mid, end):
            left = nums[start: mid + 1]
            right = nums[mid + 1: end + 1]
            i = j = 0
            k = start

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            return nums
    # sorting with merge sort
    # time complexity: O(n log n)
    # space complexity: O(n)
    # stable sort
    # not in-place sort
    # best case: O(n log n)
    # worst case: O(n log n)
    # average case: O(n log n)
    
    

# quicksort implementation in Python
class Solution(object):
    def sortArray(self, nums):
        self.Quick(nums, 0, len(nums) - 1)
        return nums
    def Quick(self, nums, start, end):
        if pivot - left + 1 <= 1:
            return nums
        pivot = nums[end]
        left = start
        for i in range(start, end):
            if nums[i] < nums[end]:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left += 1
        
        nums[end] = nums[left]
        nums[left] = pivot
        
        self.Quick(nums, start, end - 1)
        self.Quick(nums, left + 1, end)
        
        return nums
    # sorting with quicksort
    # time complexity: O(n log n) on average, O(n^2) in the worst case
    # space complexity: O(log n) for the recursive stack space
    # not a stable sort
    # in-place sort
    # best case: O(n log n) when the pivot is chosen well
    # worst case: O(n^2) when the pivot is the smallest or largest element repeatedly
    # average case: O(n log n)
        
    