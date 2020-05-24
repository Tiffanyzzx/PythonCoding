class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def invertTree(self, root):

        # Signature: input original root, output inverse root

        # base case
        if not root:
            return root

        # current level (be careful on this swag)
        temp_right = root.right
        root.right = root.left
        root.left = temp_right

        # recursive order is not important
        # left child (no return value bcuz top to bottom)
        self.invertTree(root.left)
        # right child (no return value becuz top to bottom)
        self.invertTree(root.right)

        # return value
        return root



