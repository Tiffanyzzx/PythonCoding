# Reverse a singly-linked list iteratively.

# Examples
# L = null, return null
# L = 1 -> null, return 1 -> null
# L = 1 -> 2 -> 3 -> null, return 3 -> 2 -> 1 -> null

class _ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    def reverse(self, head):
        # create a variable containing None & create a variable pointing to head
        prev = None
        curr = head

        # using a while loop, stop when curr = None
        while curr != None:
            next = curr.next  # store the remained linked list behind curr
            curr.next = prev  # disconnect the head (curr) and pointing to previous node

            # after above-mentioned steps, reassign prev and curr
            prev = curr
            curr = next
            # do not need to reassign next becuz next will be assigned to next = curr.next in following while loop
        return prev
        # why return prev not return curr?
        # the while loop stops when curr = None, and prev is pointing to the last node when curr = None
        # therefore, curr could not be returned in this reverse linked list but  prev could.

    def build_list(self, list):
        dummy_head = _ListNode(0)
        cur = dummy_head
        for x in list:
            cur.next = _ListNode(x)
            cur = cur.next
        return dummy_head.next

    def print_list(self, head):
        while head != None:
            print(head.val)
            head = head.next


# use an example to practice the reverse function
input = [1, 2, 3, 4, 5]

p1 = Solution()
head = p1.build_list(input)
reverse = p1.reverse(head)

p1.print_list(reverse)