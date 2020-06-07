class Solution(object):
  def valid(self, input):
    """
    input: string input
    return: boolean
    """
    # corner case
    if not input:
      return True
    # check palindrome: use two pointers (相向而行)
    # 没有需要改变的要求，不需要把string变成array
    left = 0
    right = len(input) - 1
    # check each single element
    while left < right:
      # 如果左右两边边遇到标点符号(不是alphanumeric characters），ignore且跳过
      if not input[left].isalnum():
        left += 1
      elif not input[right].isalnum():
        right -= 1
      # 当两边均为 alphanumeric characters 时
      # 注意大小写可以忽略不计，归类为相等
      else:
        if input[left].lower() != input[right].lower():
          return False
        else:
          left += 1
          right -= 1
      # 全部遍历结束且没有出现False，可以认定 input 是符合 palindrome 要求的
    return True