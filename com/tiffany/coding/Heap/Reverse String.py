class Solution(object):
  def reverse(self, input):
    """
    input: string input
    return: string
    """
    # corner case
    if not input:
      return input
    # transfer a string to a array(list)
    array = list(input)
    # create two pointer (相向而行)
    left = 0
    right = len(array) - 1
    # iterating the list using left & right pointers
    while left < right:
      # reverse each element
      array[left], array[right] = array[right], array[left]
      # move two pointers
      left += 1
      right -= 1
    # change the array back to a string
    return "".join(array)