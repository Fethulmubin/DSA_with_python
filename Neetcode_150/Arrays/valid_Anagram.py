class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hash_S, hash_T = {}, {}
        for char in s:
            hash_S[char] = hash_S.get(char, 0) + 1
        for char in t:
            hash_T[char] = hash_T.get(char, 0) + 1
        return hash_S == hash_T
    # time complexity: O(n)
    # space complexity: O(n)
    # where n is the length of the input strings s and t
    # we are using two hash maps to count the frequency of each character in both strings
    # and then comparing the two hash maps
    # if they are equal, then the two strings are anagrams of each other
