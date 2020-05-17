class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        one, two = self.splitInHalf(head)

        one = self.mergeSort(one)
        two = self.mergeSort(two)

        return self.merge(one, two)

    def splitInHalf(self, head):

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        next = slow.next
        slow.next = None

        return head, next

    def merge(self, one, two):

        dummy = ListNode(0)
        cursor = dummy

        while one and two:

            if one.val < two.val:
                cursor.next = one
                one = one.next
                cursor = cursor.next

            else:
                cursor.next = two
                two = two.next
                cursor = cursor.next

        if not two:
            cursor.next = one

        elif not one:
            cursor.next = two

        return dummy.next

