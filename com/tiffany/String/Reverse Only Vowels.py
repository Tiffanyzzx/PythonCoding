class Solution(object):
  def reverse(self, input):
    """
    input: string input
    return: string
    """
    # corner case
    if not input:
      return input
    # create a set of vowels for below checking(do NOT forget including ([]) )
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    # given a string (immutable), change to an array(list)
    array = list(input)
    # This is a reverse question, two pointers (相向而行）
    left = 0
    right = len(array) - 1
    # iterating each single element
    while left < right:
      if array[left] not in vowels:
        left += 1
      elif array[right] not in vowels:
        right -= 1
      else:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    # change array back to a string
    return "".join(array)


