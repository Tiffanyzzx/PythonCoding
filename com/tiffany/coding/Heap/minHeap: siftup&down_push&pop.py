class Heap(object):
    def __init__(self):
        self.array = []

    # push = append = array.append(val)
    def push(self, val):
        self.array.append(val)
        self.sift_up(self.array, len(self.array)-1)

    # remove head = remove the lowest element in minHeap
    # i) swap (head, last node)
    # ii) pop() = remove head but keep the tree is a CBT
    # iii) sift_down function to remind min-heap
    def pop(self):
        # res is the final return value
        res = self.array[0]
        # swap, make sure the tree is still a complete binary tree
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        # pop() = remove head & keet the three is a CBT
        self.array.pop()
        self.sift_down(self.array, 0)
        return res


    # sift_up:
    # i) append(push) an element into array (index = len(array) - 1 = child node)
    # ii) compare with parent index, if smaller than parent array, then swap(index, parent_idx)
    def sift_up(self, array, index):
        parent_idx = (index - 1) // 2
        # when three is None, index = 0 & parent idx < 0, return
        # if parent < idx = minHeap, return
        if parent_idx < 0 or array[parent_idx] < array[index]:
            return
        else:
            array[index], array[parent_idx] = array[parent_idx], array[index]
        # start recursion to check each level
        self.sift_up(array, parent_idx)


    # index = 0 = tree head = 1st element of array
    def sift_down(self, array, index):
        left = index * 2 + 1
        right = index * 2 +2
        # index = tree head
        small = index
        # compare tree head with left child and right child (keep min-heap)
        if left < len(array) and array[left] < array[small]:
            small = left
        if right < len(array) and array[right] < array[small]:
            small = right
        # if small has changed by last two if conditions then small != index otherwise index is the smallest element
        if small != index:
            array[small], array[index] = array[index], array[small]
            # if and only if start recursion when small != index
            # make sure small is the index for next level recursion 
            self.sift_down(array, small)


