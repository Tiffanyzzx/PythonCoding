# 方法一
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
    # change array to min-heap
    heapq.heapify(array)
    # 取 k 个最小的数值
    # min(k, len(array) 万一 k 比 len(array)还要大，两者取min
    for i in range (0, min(k, len(array))):
      current = heapq.heappop(array)
      res.append(current)
    return res