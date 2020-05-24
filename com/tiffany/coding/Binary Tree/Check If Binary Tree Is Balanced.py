# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isBalanced(self, root):
        """
        input: TreeNode root
        return: boolean
        """
        # write your solution here
        # base case
        if not root:
            return True

            # left child
        left = self.height(root.left)
        # right child
        right = self.height(root.right)
        # current level
        if abs(left - right) > 1:
            return False
            # return boolean
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        # base case
        if not root:
            return 0

        # left child
        left = self.height(root.left)
        # right child
        right = self.height(root.right)
        # current level& return
        return max(left, right) + 1
# time O(nlogn)
# space O(height)