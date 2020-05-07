# Question: Given an integer number n, find its integer square root.

# Assumption:
# n is guaranteed to be >= 0.

# Example:
# Input: 18, Return: 4
# Input: 4, Return: 2

# test example: [462959863]

class Solution(object):
    def sqrt(self, x):
        """
        input: int x
        return: int
        """
        # write your solution here

        # coner case checking
        if x == 0:
            return 0

        # set two pointers
        left = 1
        right = x

        # use BS method
        while True:
            mid = (left + right) // 2
            if mid > x // mid:
                right = mid - 1

            elif mid <= x // mid and mid + 1 > x // (mid + 1):
                return mid

            else:
                left = mid + 1

p1 = Solution()
num = 123456789
res = p1.sqrt(num)
print(res)
