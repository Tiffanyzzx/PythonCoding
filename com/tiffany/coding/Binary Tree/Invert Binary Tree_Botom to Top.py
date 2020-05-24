class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def invertTree(self, root):
        # Signature: input root with original tree & output root with inverse tree

        # base case:
        if root is None:
            return root

        # current level (Bottom to top)
        # use a temparay variable to save right root
        temp_right = root.right

        # bcuz temp_right saves root.right, so we need to start from root.right but with root.left as variable
        # there is a return value, so it needs something to accept it
        # right child
        root.right = self.invertTree(root.left)
        # left child
        root.left = self.invertTree(temp_right)

        return root

# Time: O(n)
# Space: O(logn)
