# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
    
#     Step-by-step execution:
# 1st call: reverseList(1)
# head is 1 → not None

# head.next is 2 → not None

# So: newHead = self.reverseList(2)

# 2nd call: reverseList(2)
# head is 2 → not None

# head.next is 3 → not None

# So: newHead = self.reverseList(3)

# 3rd call: reverseList(3)
# head is 3 → not None

# head.next is None

# So: newHead = head (which is 3)

# Return 3

# Now back to 2nd call:

# python
# Copy
# Edit
# newHead = 3
# head = 2
# head.next = 3

# head.next.next = head → 3.next = 2
# head.next = None → 2.next = None

# Now: 3 → 2 → None
# Return newHead (3)
# Now back to 1st call:

# python
# Copy
# Edit
# newHead = 3
# head = 1
# head.next = 2

# head.next.next = head → 2.next = 1
# head.next = None → 1.next = None

# Now: 3 → 2 → 1 → None
# Return newHead (3)