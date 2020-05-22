class Solution(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self._size = 0
        self._items = [None] * (k + 1)
        # first always pts to the position where we will insert the new front element of this queue
        self._first = 0
        # last always pts to the position where insert the new reer element of this queue
        self._last = 1

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self._items[self._first] = value
        self._first = (self._first - 1 + len(self._items)) % len(self._items)
        self._size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self._items[self._last] = value
        self._last = (self._last + 1) % len(self._items)
        self._size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self._first = (self._first + 1) % len(self._items)
        self._size -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self._last = (self._last - 1 + len(self._items)) % len(self._items)
        self._size -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return False

        else:
            return self._items[(self._first + 1) % len(self._items)]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return False

        else:
            return self._items[(self._last - 1 + len(self._items)) % len(self._items)]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self._size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self._size == len(self._items) - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
