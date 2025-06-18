# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
      l = 1
      for r in range(1, len(nums)):
        if(nums[r] != nums[r - 1]):
            nums[l] = nums[r]
            l += 1
      return l
        
# https://leetcode.com/problems/remove-element/
class Solution(object):
    def removeElement(self, nums, val):
       k = 0
       for i in range(len(nums)):
            if(nums[i] != val):
                nums[k] = nums[i]
                k += 1
       return k


# https://leetcode.com/problems/shuffle-the-array/
class Solution(object):
    def shuffle(self, nums, n):
        formed = []
        for i in range(n):
            formed.append(nums[i])
            formed.append(nums[i + n])
        return formed
