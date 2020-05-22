class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def post_order(self,root):
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        # base case
        if root is None:
            return

        # post-order recursion
        self.traverse(root.left, res)
        self.traverse(root.right, res)
        res.append(root.val)
        return