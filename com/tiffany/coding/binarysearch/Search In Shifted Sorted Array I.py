class Solution(object):
    def search(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        if not array:
            return -1
        left = 0
        right = len(array) - 1
        # search each single element existing in the array
        while left <= right:
            mid = (left + right) // 2
            # if mid = target
            if array[mid] == target:
                return mid
                # 假设左半边有序
            if array[left] <= array[mid]:
                # 首先先检查 target 在 sorted region 里 (left < targt < mid)
                # 注意 target 是有可能等于 array[left]
                if array[left] <= target and target < array[mid]:
                    # 缩小范围
                    # 不能写 right = mid。假设最后只剩下两个elements 则不能通过
                    right = mid - 1
                # 如果 taregt 不在 sorted region 里
                else:
                    left = mid + 1
            # 假设右半边有序
            else:
                # 首先先检查 target 在 sorted region 里 (mid < target < right)
                # 假设 target 是有可能等于 array[right]
                if array[mid] < target and target <= array[right]:
                    # 缩小范围
                    left = mid + 1
                # 如果 taregt 不在 sorted region 里
                else:
                    right = mid - 1
        # 如果 array 里没有 target number
        return -1
