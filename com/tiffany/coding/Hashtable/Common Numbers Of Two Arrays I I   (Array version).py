# Question:
# Find all numbers that appear in both of two unsorted arrays.

# Assumptions
# Both of the two arrays are not null.
# In any of the two arrays, there could be duplicate numbers.

# Examples
# A = {1, 2, 3, 2}, B = {3, 4, 2, 2, 2}, return [2, 2, 3]

class Solution(object):
    def common(self, A, B):
        """
        input: int[] A, int[] B
        return: Integer[]
        """
        # write your solution here

        # create a dictionary
        a_dict = {}

        # iterate each elements in array A into the above-created dictionary
        for num in A:
            a_dict[num] = a_dict.get(num, 0) + 1

        # do these processes again for array B
        b_dict = {}

        for num in B:
            b_dict[num] = b_dict.get(num, 0) + 1

        # create a list to collect all numbers that appear in both of two arrays
        common = []

        for num in a_dict:
            common += [num] * min(a_dict[num], b_dict.get(num, 0))

        return common

p1 = Solution()
a = [9,9,8,7,6,5,3,2,8,1,9,100]
b = [9,9,8,19,5,21,1,9,8,4,100]

res = p1.common(a, b)
print(res)