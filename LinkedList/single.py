
# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: [ListNode]) -> [ListNode]:
#         prev, cur = None, head
#         while cur:
#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt
#         return prev
    
# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # Output: 0
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

# Example usage:
# Create first sorted linked list: 1 -> 2 -> 4
l1 = ListNode(1, ListNode(2, ListNode(4)))
# Create second sorted linked list: 1 -> 3 -> 4
l2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge the two lists
sol = Solution()
merged_head = sol.mergeTwoLists(l1, l2)
# Print all values in the merged linked list
current = merged_head
while current:
    print(current.val, end=" ")
    current = current.next
print()

# key concepts:

# dummy: This is a placeholder node at the start of your merged list. It doesn't hold meaningful data; it's just there to simplify the logic.
# tail: This is a moving pointer that always points to the last node in your merged list as you build it.
# Why dummy.next Returns the Whole List
# dummy always points to the start of your merged list (the placeholder node).
# dummy.next points to the real head of your merged list (the first actual data node).
# When you return dummy.next, you return the entire merged list (excluding the dummy node).
# Why tail.next Might Only Return 4
# tail moves as you build the list. At the end, tail points to the last node (which, in your example, has value 4).
# tail.next is None (since it's the end of the list), or if you set it to something else, it could point to a single node.
# So, returning tail.next gives you only what's after the last node—usually nothing, or just the last node if you made a mistake.
# Analogy
# Think of dummy as a coat hanger and tail as your hand moving along the clothes as you hang them. At the end, your hand is at the last shirt, but the hanger still holds the whole row.

# Example
# Suppose you have this code:

# Summary
# Return dummy.next to get the full merged list.
# Return tail.next only gives you what's after the last node (usually nothing).
# Let me know if you want to see a code example!

# https://leetcode.com/problems/design-linked-list/
# it is bets to do it using doubly linkedlist but in my case i done with singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        new_node = Node(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
