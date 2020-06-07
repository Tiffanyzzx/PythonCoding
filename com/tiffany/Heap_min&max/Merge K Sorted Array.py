import heapq


class Solution(object):
    def merge(self, arrayOfArrays):
        """
        input: int[][] arrayOfArrays
        return: int[]
        """
        # Two steps:
        # (1) 把 arrayOfArrays 里每一组 array 里的第一个 element 加入 list 再 heapify
        # (2) min-heap 里 head 为最小值，每次取出加入 result list & 回到 arrayOfArrays 里去找是哪一个 array 并且把下一个值 heappush

        # （1）
        heap = []
        # row = len(matrix)
        # column = len(matrix[0])
        for i in range(len(arrayOfArrays)):
            # make sure each array is not empty
            # use column, check 1st element is existing
            if len(arrayOfArrays[i]):
                # arrayOfArrays[i][0] = value
                # i = row #
                # 0 = column #
                # dont forget (())
                heap.append((arrayOfArrays[i][0], i, 0))
                # 根据 arrayOfArrays[i][0] 里的 value 做了一个 min-heap
                heapq.heapify(heap)

                # （2）
                res = []
        while heap:
            # arrayOfArrays[i][0] = value
            # i = row #
            # 0 = column #
            value, index_row, index_column = heapq.heappop(heap)
            res.append(value)
            # make sure index_column + 1 is not out of boundry
            if index_column + 1 < len(arrayOfArrays[index_row]):
                # do not forget (())
                heapq.heappush(heap, (arrayOfArrays[index_row][index_column + 1], index_row, index_column + 1))
        return res





