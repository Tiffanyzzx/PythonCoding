# Given a target integer T and an integer array A sorted in ascending order,
# find the index i such that A[i] == T or return -1 if there is no such index.

# Assumptions
# There can be duplicate elements in the array, and you can return any of the indices i such that A[i] == T.

# Examples
# A = {1, 2, 3, 4, 5}, T = 3, return 2
# A = {1, 2, 3, 4, 5}, T = 6, return -1
# A = {1, 2, 2, 2, 3, 4}, T = 2, return 1 or 2 or 3

# Corner Cases
# What if A is null or A is of zero length? We should return -1 in this case.

class Solution():

    def binary_search(self, array, target):

        # write your solution here
        if array == None or len(array) == 0:
            return -1
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


# one way to use the class:
p1 = Solution()  # create an object 1st
array = [3, 4, 5, 5, 6, 9, 16]
target = 9
res = p1.binary_search(array, target)  # variable
print(res)


# another way to use the class:
def main():
    p1 = Solution()  # create an object 1st
    array = [3, 4, 5, 5, 6, 9, 16]
    target = 5
    res = p1.binary_search(array, target)  # variable
    print(res)


main()
