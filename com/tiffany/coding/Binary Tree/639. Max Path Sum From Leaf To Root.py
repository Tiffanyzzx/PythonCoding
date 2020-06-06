class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
  def maxPathSumLeafToRoot(self, root):
    """
    input: TreeNode root
    return: int
    """
    # two base cases
    # 1st: when root = None
    if not root:
      return -float('inf')
    # 2nd: since root = None return -inf, write another base case for leaf node
    if root.left == None and root.right == None:
      return root.val
    # left child
    left = self.maxPathSumLeafToRoot(root.left)
    # right child
    right = self.maxPathSumLeafToRoot(root.right)
    # return value
    return max(left, right) + root.val
