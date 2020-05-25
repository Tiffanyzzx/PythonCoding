class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def pre_order(self, root):
        # Signature: input root & output list

        # create a list
        res = []
        # corner case
        if not root:
            return res

        # create a stack
        stack = []
        # let stack not be empty
        stack.append(root)
        while stack:
            curr_root = stack.pop()
            # right root has to be first
            if curr_root.right:
                stack.append(curr_root.right)
            if curr_root.left:
                stack.append(curr_root.left)
            res.append(curr_root.val)
        return res


