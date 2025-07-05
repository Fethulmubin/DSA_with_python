from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groupedAnagrams = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            groupedAnagrams[tuple(count)].append(word)
            print(groupedAnagrams[tuple(count)])
        return list(groupedAnagrams.values())
    
# how it works:
# 1. We use a defaultdict to group anagrams together.
# 2. For each word, we create a count of characters (a list of size 26 for each letter in the alphabet).
# 3. We convert this count to a tuple (to use it as a key in the dictionary) and append the word to the corresponding list.
# 4. Finally, we return the values of the dictionary as a list of lists containing grouped anagrams.

# groupedAnagrams seems like : 
# {
#  (1,0,0,0,1,0,...,1): ['eat', 'tea', 'ate'],
#  (1,0,0,1,0,...,1): ['tan', 'nat'],
#  (1,1,0,0,0,...,1): ['bat']
# }
sol = Solution()
# Example usage:
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# Explanation: The function groups the anagrams together in lists.


# bucket sort approach:# from collections import defaultdict
# https://leetcode.com/problems/sort-colors/
class Solution(object):
    def sortColors(self, nums):
        count = [0, 0, 0]
        for i in nums:
            count[i] += 1
        i = 0
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i += 1
        return nums
# Example usage:
sol = Solution()
print(sol.sortColors([2, 0, 2, 1, 1, 0]))
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: The function sorts the colors in-place using a counting sort approach.
# This code defines a class Solution with a method groupAnagrams that groups anagrams from a list of strings.