class Solution(object):
    def containsDuplicate(self, nums):
        viewd = []
        for num in nums:
            if num in viewd:
                return True
            viewd.append(num)
        return False
    
    # time limit for the above exceeds for large inputs
    # but for the below solution, it passes all test cases
    class Solution(object):
        def containsDuplicate(self, nums):
            seen = set()
            for num in nums:
                if num in seen:
                    return True
                seen.add(num)
            return False