# Determine if a given binary tree is binary search tree.There should no be duplicate keys in binary search tree.

# Assumptions：
# You can assume the keys stored in the binary search tree can not be Integer.MIN_VALUE or Integer.MAX_VALUE.
# Corner Cases
# What if the binary tree is null? Return true in this case.

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def isBST(self, root):
        # Signature: input root & output boolean

        # let min = -inf & max = inf
        min = float("-inf")
        max = float('inf')
        return self.helper(root, min, max)

    def helper(self, root, min, max):
        # base case
        if not root:
            return True

        # left child & right child : (-inf, root) & (root, inf)
        # (-inf, root) & (root, inf)， top to bottom, 注意取值是每一层 sub question 里需要满足 BST 的要求
        if root.val <= min or root.val >= max:
            return False

        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)



# time: O(n)
# space: O(h)
