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
