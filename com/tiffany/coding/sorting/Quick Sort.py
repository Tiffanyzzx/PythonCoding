class Solution(object):
    def partition(self, alist, left, right):

        # set two pointers to pt the index of left and right - 1
        start = left  # index
        end = right - 1  # index

        # import a method to randomly pick a index
        import random
        # use a variable to collect the randomly picked index between left and right
        rant = random.randint(left, right)
        # swap the rant to the last index of the current array
        alist[rant], alist[right] = alist[right], alist[rant]

        # use a variable, pivot, to represent the VALUE of the rant, which has been swapped with right from above-mentioned step
        pivot = alist[right]

        # start a while loop, which will be ended after iterating the entire array
        while start <= end:  # start&end represent indexes.
            if alist[start] < pivot:  # start is an indext but pivot is a value
                start += 1
            elif alist[end] >= pivot:  # "<=" is using for iterating the array, plus above if statment is using "<"
                end -= 1
            else:  # elif: alist[start]>=pivot and alist[end]<pivot
                alist[start], alist[end] = alist[end], alist[start]  # swap them
                start += 1
                end -= 1  # let both of them move a step

        # when the entire while loop stopped, start > end, it is where the start located at a index which is the first value
        # bigger than the pivot. Therefore, we could directly swap this value with the pivot
        alist[start], alist[right] = alist[right], alist[start]  # we need to use right to swap, cannot use pivot since its a value
        return start


    def quick_sort(self, alist, left, right):

        # base case for following recursion
        if left > right:  # when the recursion hits the end where does not have any elements remained
            return

        pivot = self.partition(alist, left, right)  # make sure the index of the first pivot and separate the array into two parts
        self.quick_sort(alist, left, pivot - 1)  # recursion of the left side of the lastest pivot
        self.quick_sort(alist, pivot + 1, right)  # recursion of the right side of the lastest pivot

    def quickSort(self, array):
        """
        input: int[] array
        return: int[]
        """

        # write your solution here

        self.quick_sort(array, 0, len(array) - 1)
        return array


a = [1, 4, 3, 2, 5, 6]
p1 = Solution()
res = p1.quickSort(a)
print(a)
print(res)
