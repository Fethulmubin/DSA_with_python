# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root
# The searchBST function performs a binary search on a binary search tree (BST).
# It recursively traverses the tree, comparing the current node's value with the target value (
# val). If the current node's value is greater than val, it searches in the left subtree; if it's less,
# it searches in the right subtree. If it finds a node with the value equal to val, it returns that node.
# If the value is not found, it returns None. This function assumes that the input tree is a valid BST, where for each node, all values in the left subtree are less than the node's value,
# and all values in the right subtree are greater than the node's value.
# This approach has a time complexity of O(h), where h is the height of the tree, and a space complexity of O(h) due to the recursive call stack.
# Example usage:
# root = TreeNode(4)    
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# solution = Solution()
# result = solution.searchBST(root, 2)
# if result:
#     print("Found:", result.val)
# else:
#     print("Not found")
# This will output: Found: 2

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
# The lowestCommonAncestor function finds the lowest common ancestor of two nodes (p and q) in a binary search tree (BST).
# It works by comparing the values of p and q with the value of the current root node
# (root). If both p and q are less than root, it recursively searches in the left subtree.
# If both are greater, it searches in the right subtree. If one is on one side and the other is on the other side,
# or if one of them is equal to the root, then the current root is the lowest common ancestor.
# This function assumes that both p and q are present in the tree.
# The time complexity is O(h), where h is the height of the tree, and the space complexity is O(h) due to the recursive call stack.
# the else condition handles the case where they split this means 
# p < root < q or p > root > q or one of them is equal to root
# Example usage:
