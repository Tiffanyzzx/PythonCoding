# Question：Given a 2D matrix that contains integers only, which each row is sorted in an ascending order.
# The first element of next row is larger than (or equal to) the last element of previous row.

# Given a target number, returning the position that the target locates within the matrix.
# If the target number does not exist in the matrix, return {-1, -1}.

# Assumptions:
# The given matrix is not null, and has size of N * M, where N >= 0 and M >= 0.

# Examples:
# matrix = { {1, 2, 3}, {4, 5, 7}, {8, 9, 10} }
# target = 7, return {1, 2}

# target = 6, return {-1, -1} to represent the target number does not exist in the matrix.

# test example: matrix = [[[]]
# target = 100

class Solution ():
    def search(self, matrix, target):

        # step 1: corner case checking
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return [-1, -1]

        # step 2: identify row and column
        row = len(matrix)
        col = len(matrix[0])

        # step 3: using binary search, converting between 1D array & 2D matrix
        # 3.1: identify left and right in 1D array
        left = 0
        right = row * col - 1

        # 3.2: use binary search to remain one item
        while left <= right:
            mid = (left + right) // 2 # calc mid in 1D array
            x = mid // col # convert which row the calculated mid is located in 2D matrix
            y = mid % col # convert which column the calculated mid is located in 2D matrix
            if matrix[x][y] == target:
                return [x,y]
            elif matrix[x][y] < target:
                left = mid + 1
            elif matrix[x][y] > target:
                right = mid - 1
        return [-1,-1]

p1 = Solution()
matrix = []
target = 100
res = p1.search(matrix, target)
print(res)