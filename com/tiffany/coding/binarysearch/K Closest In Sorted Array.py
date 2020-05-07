class Solution(object):
    def kClosest(self, array, target, k):
        """
        input: int[] array, int target, int k
        return: int[]
        """
        # write your solution here
        if array == None or len(array) == 0:
            return None

        if k < 0 or k > len(array):
            return None

        left = 0
        right = len(array) - 1

        while left < right - 1:
            mid = (left + right) // 2
            if target <= array[mid]:
                right = mid
            else:
                left = mid

        result = list([0] * k)
        i = 0
        while i < k:
            if (right > len(array) - 1) or (left >= 0 and abs(array[left] - target) <= abs(array[right] - target)):
                result[i] = array[left]
                left -= 1

            else:
                result[i] = array[right]
                right += 1

            i += 1

        return result

p1 = Solution()
array = [1, 2, 2, 2, 4, 5, 8, 13, 13]
target = 5
k = 3
res = p1.kClosest(array, target, k)
print(res)
