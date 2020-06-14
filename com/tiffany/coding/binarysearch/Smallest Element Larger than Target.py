class Solution(object):
  def smallestElementLargerThanTarget(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # corner case
    if not array:
      return -1
    # set two pts
    left = 0
    right = len(array) - 1
    # remain two elements after the while loop for post processing
    while left < right - 1:
      mid = (left + right) // 2
      # 因为最后需要剩余两个elements求大于且最接近target的数值，不能写 array[mid] == target, return mid
      if array[mid] <= target:
        left = mid
      elif array[mid] > target:
        right = mid
    # post processing (记得写大于号，不是等于号)
    if array[left] > target:
      return left
    elif array[right] > target:
      return right
    # 如果没有此结果，return -1
    return -1