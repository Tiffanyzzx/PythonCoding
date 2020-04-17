class _ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def _get(self, index):
        cursor = self._head
        for x in range(index):
            cursor = cursor.next
        return cursor

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self._size:
            return -1
        return self._get(index).val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            new_head = _ListNode(val)
            new_head.next = self._head
            self._head = new_head

        self._size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            self._tail.next = _ListNode(val) # self._tail.next is None, let None connect to new node first
            self._tail = self._tail.next # assign self._tail to new node
        self._size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index >= self._size:
            return -1
        if self._size == 0:
            self.addAtHead(val)
        elif index == self._size:
            self.addAtTail(val)
        else:
            cursor = self._get(index - 1)
            new_node = _ListNode(val)
            new_node.next = cursor.next
            cursor.next = new_node
            self._size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self._size:
            return -1
        if index == 0:
            new_head = self._head.next  # store self._head.next
            self._head.next = None
            self._head = new_head
            # If the last one was getting removed, self._tail needs removed as well
            if not self._head:  # if self._head is not existing anymore
                self._tail = None
        else:
            cursor = self._get(index - 1)
            remove_node = cursor.next  # store the node which is gonna be removed
            cursor.next = remove_node.next
            remove_node.next = None
            # What if I remove the original tail (the last node in the linked list)
            if index == self._size - 1:
                self._tail = cursor  # tail needs to be assigned if we are removing the last node
        self._size -= 1

    def __str__(self):
        strs = []
        cursor = self._head
        while cursor is not None:
            strs.append(str(cursor.val))
            cursor = cursor.next
        return "->".join(strs)