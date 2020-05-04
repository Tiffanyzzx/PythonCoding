# Question
# Find all numbers that appear in both of the two unsorted arrays, return the common numbers in increasing order.

# Assumptions
# Both arrays are not null.
# There are no duplicate numbers in each of the two arrays respectively.

#Exmaples
# A = {1, 2, 3}, B = {3, 1, 4}, return [1, 3]
# A = {}, B = {3, 1, 4}, return []

class Solution(object):
    def common(self, a, b):
        """
        input: int[] a, int[] b
        return: Integer[]
        """
        # write your solution here

        # As the request mentioned, there are no duplicated numbers in each of the two arrays
        # find commom numbers in increasing order
        # therefore, the first step should be change one of the arrays to be a set. a or b could both work.
        # definition of a set: unsorted, unindexed & NO duplicated values
        s = set(a)

        # for x in b:
        #   if x in s:
        #     return x
        # above codes do not match request
        # this question is asking return the common numbers in increasing order. return a sorted array.

        return sorted(x for x in b if x in s)
        # for x in b, iterating all elements contained inside of the b array
        # if x in b is also exiting in s, a set with No dublicated elements.
        # return x elements. If there are more common numbers then return a sorted x array


p1 = Solution()
a = [9,8,7,6,5,3,2,1,100]
b = [19,5,21,1,8,4,100]

res = p1.common(a, b)
print(res)