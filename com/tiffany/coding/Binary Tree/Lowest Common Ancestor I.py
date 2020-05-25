# Given two nodes in a binary tree, find their lowest common ancestor

# Assumptions
# There is no parent pointer for the nodes in the binary tree
# The given two nodes are guaranteed to be in the binary tree

# Examples
#
#         5
#
#       /   \
#
#      9     12
#
#    /  \      \
#
#   2    3      14
#
# The lowest common ancestor of 2 and 14 is 5
# The lowest common ancestor of 2 and 9 is 9


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    # Signature:
    # input: one root and two given roots
    # output: one root (the lowest Common Ancester)
    def lowestCommonAncester(self, root, root2, root3):

        # two recursion base cases
        if not root:
            return None
        if root == root2 or root == root3:
            return root

        # left child
        left_res = self.lowestCommonAncester(root.left, root2, root3)
        # right child
        right_res = self.lowestCommonAncester(root.right, root2, root3)

        # current level
        if left_res and right_res:
            return root
        elif left_res:
            return left_res
        elif right_res:
            return right_res



