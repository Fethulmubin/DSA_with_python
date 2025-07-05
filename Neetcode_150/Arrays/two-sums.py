# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        # Create an empty dictionary (hashmap) to store seen numbers and their indices
        hashmap = {}

        # Loop through the array using enumerate to get both index (i) and value (num)
        for i, num in enumerate(nums):
            # Calculate the number needed to reach the target from current number
            complement = target - num

            # Check if this complement was already seen (i.e., exists in hashmap)
            if complement in hashmap:
                # If yes, return the indices of the complement and current number
                # The complement's index comes first (from hashmap), then the current index
                return [hashmap[complement], i]

            # If complement is not found, store the current number and its index in hashmap
            # So we can look it up later when its complement appears
            hashmap[num] = i
