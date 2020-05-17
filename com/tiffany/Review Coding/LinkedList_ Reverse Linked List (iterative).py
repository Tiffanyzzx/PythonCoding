class _ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():

    def reserveLinkedList(self, head):

        prev = 0
        cursor = head

        while cursor != None:
            next = cursor.next
            cursor.next = prev

            prev = cursor
            cursor = next

        return prev
