class Solution(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        # 开辟一个区域 as a container
        self.elems_ = [None] * (k + 1)

        # Since this is a Que, there must be a head and a tail
        self.head_ = self.tail_ = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.elems_[self.tail_] = value
        self.tail_ = (self.tail_ + 1) % len(self.elems_)
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head_ = (self.head_ + 1) % len(self.elems_)
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.elems_[self.head_]
        else:
            return False

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.elems_[(self.tail_ - 1 + len(self.elems_)) % len(self.elems_)]
        else:
            return False

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.head_ == self.tail_

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return (self.tail_ - self.head_ + len(self.elems_)) % len(self.elems_) == len(self.elems_) - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
