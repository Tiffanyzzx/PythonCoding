# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# For testing purpose, please make sure for any node in the result, its left sub-tree should have equal or only one more node than its right sub-tree.
# Example:
#     Given ascending order list: 1→3→4→5→8→11
#
#     return Binary Search Tree is
#
#               5
#
#           /        \
#
#         3          11
#
#     /      \      /
#
#   1        4    8


class ListNoe():
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def sortedListToBST(self, head):
        if not head:
            return Noen
        tail = None
        return self.helper(head, tail)

    def helper(self, head, tail):
        if head == tail:
            return None
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        root = TreeNode(mid.val)
        root.left = self.helper(head, mid)
        root.right = self.helper(mid.next, tail)
        return root
