# Given a binary tree and a target sum,
# determine if the tree has a root-to-leaf path such that
# adding up all the values along the path equals the given target.

# important: root to leaf (一整条线加起来） & add up ALL values along the path

# Example:
# Given the below binary tree and target = 16,
#
#               5
#              / \
#             4   8
#            /   / \
#           1    3  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5-8-3 which sum is 16.

class ThreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    # Signature: input root and target & output boolean
    def sum_to_target(self, root, target):
        # corner case
        if not root:
            return False
        # return value: Boolean but use another method which contain three variables
        return self.sumPath(root, 0, target)

    def sumPath(self, root, sum, target):
        # base case
        if root is None:
            return False
        # current level
        sum = sum + root.val
        if root.left is None and root.right is None:
            if sum == target:
                return True
        # left child & right child (注意调用里需要有三个对象：root.left/right, sum, and target)
        left = self.sumPath(root.left, sum, target)
        right = self.sumPath(root.right, sum, target)

        # return value (boolean)
        return left or right
