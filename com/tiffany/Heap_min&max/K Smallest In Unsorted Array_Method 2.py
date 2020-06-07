# 方法二
import heapq
class Solution(object):
  def kSmallest(self, array, k):
    """
    input: int[] array, int k
    return: int[]
    """
    # create an array to collect Kth smallest elements
    res = []
    # corner case,
    if not array:
      return res
    # make sure k is in a valid range
    if k >= len(array):
      return array
    # change array to min-heap
    heapq.heapify(array)
    # 取 k 个最小的数值
    for i in range (0, k):
      current = heapq.heappop(array)
      res.append(current)
    return res