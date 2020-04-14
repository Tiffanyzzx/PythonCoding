# Question: Single list implementation

class _ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # semantics for self._head: it will always refer to the head node
        # create internal single linked list
        self._head = None

        # semantics for self._size: it will always refer to the numbers of nodes contained inside of the linked list
        # create an initial number of node
        self._size = 0

        # it is pointing to the last one,
        self._tail = None


    # assuming index is within [0, self._size)
    def _get(self, index):
        node = self._head
        for _ in range(index):
            node = node.next
        return node


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
        Add a node of value val before the first element of the linked list. After the insertion,
        the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            new_head = _ListNode(val) # create a new node as a new object
            new_head.next = self._head # let the new node (its pointer) to point self.head
            self._head = new_head  # let self.head to connect the new head (its value)
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
            new_head