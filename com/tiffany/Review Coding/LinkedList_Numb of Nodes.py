# Return the number of nodes in the linked list.
#
# Examples
# L = null, return 0
# L = 1 -> null, return 1
# L = 1 -> 2 -> null, return 2

class ListNode():
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution():
    def numberOfNodes(self, head):
        cursor = head
        num = 0

        while cursor != None:
            num += 1
            cursor = cursor.next

        return num