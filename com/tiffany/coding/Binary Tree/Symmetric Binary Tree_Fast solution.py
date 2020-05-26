class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def isBT(self, root):
        if not root:
            return True
        res = self.helper(root)
        if res == -1:
            return False
        else:
            return True

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if abs(left - right) > 1:
            return -1
        if left == -1 or right == -1:
            return -1
        return max(left, right) + 1