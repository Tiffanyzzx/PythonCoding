# Given an array of integers, sort the elements in the array in ascending order. The merge sort algorithm should be used to solve this problem.

# Examples
# {1} is sorted to {1}
# {1, 2, 3} is sorted to {1, 2, 3}
# {3, 2, 1} is sorted to {1, 2, 3}
# {4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}

# Corner Cases
# What if the given array is null? In this case, we do not need to do anything.
# What if the given array is of length zero? In this case, we do not need to do anything.

class Solution(object):
    def mergeSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here

        # corner check & base check for following recursion
        if len(array) <= 1:
            return array

            # cut the array to half
        mid = len(array) // 2

        # identify left/righ half & start recursion to let the array break down to single element
        left_half = self.mergeSort(array[:mid])
        right_half = self.mergeSort(array[mid:])

        # use the merge method to sort these separated elements
        return self.merge(left_half, right_half)

    # write a merge method
    def merge(self, left_half, right_half):

        # set up some initial variables
        i = 0
        j = 0

        # set a new list while is used for collecting sorted elements
        alist = []

        # when left_half and right_half are both having elements
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                alist.append(left_half[i])
                i += 1

            elif left_half[i] > right_half[j]:
                alist.append(right_half[j])
                j += 1

        # when only left_half array has elements left
        while i < len(left_half):
            alist.append(left_half[i])
            i += 1

        # when only right_half array has elements left
        while j < len(right_half):
            alist.append(right_half[j])
            j += 1

        # return the new merged/sorted list
        return alist

a = [1, 4, 3, 2, 5, 6]
p1 = Solution()
res = p1.mergeSort(a)
print(res)