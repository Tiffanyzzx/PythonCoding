class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def in_order(self, root):
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        # base case
        if root is None:
            return

        # in-order process
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)
        return