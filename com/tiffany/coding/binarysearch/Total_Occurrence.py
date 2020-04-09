# Given a target integer T and an integer array A sorted in ascending order,
# Find the total number of occurrences of T in A.

# Examples
# A = {1, 2, 3, 4, 5}, T = 3, return 1
# A = {1, 2, 2, 2, 3}, T = 2, return 3
# A = {1, 2, 2, 2, 3}, T = 4, return 0

# Corner Cases
# What if A is null? We should return 0 in this case.

class Solution():
    def totalOccur(self, array, target):

        # step 1: corner case checking
        if not array:
            return 0

        # step 2: create objects based on above-mentioned class & identify final returns
        firstOccur = self.firstOccur(array, target) # go to step 3
        lastOccur = self.lastOccur(array, target) # go to step 4

        if lastOccur == -1:
            return 0
        else:
            return lastOccur - firstOccur + 1

    # step 3: construct first occurrence framework to look for the index of 1st target
    def firstOccur(self, array, target):
        # 3.1: corner case checking
        if not array:
            return -1

        # 3.2: binary search, remain two two closest items
        left = 0
        right = len(array) - 1

        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] >= target:
                right = mid
            elif array[mid] < target:
                left = mid

        # 3.3: post processing, check left item first
        if array[left] == target:
            return left
        elif array[right] == target:
            return right
        else:
            return -1

    # step 4: construct last occurrence framework to look for the index of last target
    def lastOccur(self, array, target):
        # 4.1: corner case checking
        if not array:
            return -1

        # 4.2: binary search, remain two two closest items
        left = 0
        right = len(array) - 1

        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] <= target:
                left = mid
            elif array[mid] > target:
                right = left

        # 4.3: post processing, check right item first
        if array[right] == target:
            return right
        elif array[left] == target:
            return left
        else:
            return -1

# running an example
p1 = Solution()
array = [1,2,2,2,4,5,8,13,13]
target = 13
res = p1.totalOccur(array, target)
print(res)

