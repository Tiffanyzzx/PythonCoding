class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def preorder(self, root):
        res = []
        stack = []
        if not root:
            return res
        stack.append(root)
        while stack:
            current = stack.pop()
            if current.right:
                stack.append(current.left)
            if current.left:
                stack.append(current.right)
            res.append(current.val)
        return res 