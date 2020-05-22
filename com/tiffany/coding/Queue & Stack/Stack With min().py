# Enhance the stack implementation to support min() operation.
# min() should return the current minimum value in the stack. If the stack is empty, min() should return -1.

# push(int element) - push the element to top
# pop() - return the top element and remove it, if the stack is empty, return -1
# top() - return the top element without remove it, if the stack is empty, return -1
# min() - return the current min value in the stack.

class Solution(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []
        self._mins = []

    def push(self, x):
        """
        input : int x
        return :
        """
        self._items.append(x)
        # self._mins[-1] >= x 可以保证 self._mins 这个container里可以有多个elements，但是最后一个 element 一定是最小的
        if not self._mins or self._mins[-1] >= x:
            self._mins.append(x)

    def pop(self):
        """
        return : int
        """
        if not self._items:
            return -1

        # 如果 pop 出来的 element 和 min 的最后一个一样，那也把min container里的最后一个弄掉
        item = self._items.pop()
        if item == self._mins[-1]:
            self._mins.pop()
        return item

    def top(self):
        """
        return : int
        """
        if self._items:
            return self._items[-1]
        else:
            return -1

    def min(self):
        """
        return : int
        """
        # self._mins 这个container里可以有多个elements，但是最后一个 element 一定是最小的
        if self._mins:
            return self._mins[-1]
        else:
            return -1
