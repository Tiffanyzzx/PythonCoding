class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def is_symmetric(self, root):
        # Signature: input root & return boolean

        # corner case
        if not root:
            return True

        # return value
        result = self.helper(root.left, root.right)
        return result

    def helper(self, root1, root2):

        # Three base cases & they have to be in order & they have to be three if statements（同级）
        # 1st: if left child and right child are not None, return true
        # 2nd: if one of the left and right is None, return false
        # 3rd: left child's value != right child value, return false
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        # for symmetric tree, root1.left = root2.right & root1.right = root2.left
        # left child
        left_child = self.helper(root1.left, root2.right)
        # right child
        right_child = self.helper(root1.right, root2.left)

        # current level
        current = left_child and right_child

        # return value
        return current

# Time: O(n)
# Space: O(height)
