# Question: Reverse a singly-linked list recursively.

# Examples
# L = null, return null
# L = 1 -> null, return 1 -> null
# L = 1 -> 2 -> 3 -> null, return 3 -> 2 -> 1 -> null


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def reverse(self, head):
        """"
        input: ListNode head
        return ListMode
        """

        # base case for the linked list
        # if the linked list is None or only having one node, then return the head
        # if the linked list is having many node existing, check the following recursion
        if not head or not head.next:
            return head

        # using a recursive method to iterate the entire linked list
        # the "head.next" will assign to method (def reverse) as head
        # when the recursion hits head.next = None, it will stop and return head to last run
        new_head = self.reverse(head.next)
        # when finishing the recursion, the new_head is equal to the last node cuz it is when the recursion stopped


        # below codes will only happen after the recursion getting stopped
        # think it is the process you would like each step to do ( better use the beginning node to imagine)
        head.next.next = head
        head.next = None

        # we have to return from the last node of this linked list
        return new_head
        # when finishing the recursion, the new_head is equal to the last node cuz it is when the recursion stopped

    # build another method to build the linked list
    def build_list(self, list):
        dummy_head = ListNode(0)
        cur = dummy_head
        for x in list:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy_head.next

    # print method
    def print_list(self, head):
        while head != None:
            print(head.val)
            head = head.next



# use an example to practice the reverse function
input = [1, 2, 3, 4, 9, 6, 5]

p1 = Solution()
head = p1.build_list(input)
reverse = p1.reverse(head)

p1.print_list(reverse)