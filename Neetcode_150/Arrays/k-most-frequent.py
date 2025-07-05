# https://leetcode.com/problems/top-k-frequent-elements/
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}

        # Step 1: Count frequency
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            bucket[c].append(n)

        # Step 3: Gather top k frequent elements
        # starting from largest frequency to get most frequents 
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
