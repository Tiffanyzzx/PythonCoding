class Solution(object):
    def search(self, matrix, target):
        """
        input: int[][] matrix, int target
        return: int[]
        """
        # write your solution here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return [-1, -1]

        row = len(matrix)
        column = len(matrix[0])

        left = 0
        right = row * column - 1

        while left <= right:
            mid = (left + right) // 2

            x = mid // column
            y = mid % column

            if target == matrix[x][y]:
                return [x, y]
            elif target < matrix[x][y]:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]

matrix = [[1,2,3],[3,4,5]]
target = 3
p1 = Solution()
res = p1.search(matrix, target)
print(res)