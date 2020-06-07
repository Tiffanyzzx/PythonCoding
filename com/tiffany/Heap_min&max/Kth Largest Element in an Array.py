
import heapq

class Solution(object):
  def findKthLargest(self, array, k):
    """
    input: int[] nums, int k
    return: int
    """
    # corner case
    if not array:
      return None
    # if K is not valid
    if k > len(array):
      return None
    # 建立一个 min-heap（array）摘取array里0-k的数值
    min_heap = array[0:k]
    heapq.heapify(min_heap)
    # 遍历array里在k之后的每一个数值，每一个value都和min_heap的最小值做比较
    # 如果array里有比minheap大的，就替换
    for i in array[k:]:
      if min_heap[0] < i:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, i)
    # 遍历完之后，留在min heap顶端的tree head就是 Kth largest element
    return min_heap[0]

