# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def preOrder(self, root):
        """
        input: TreeNode root
        return: Integer[]
        """
        # write your solution here
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        # base case
        if root is None:
            return

            # pre-order recursion process
        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)
        return

p1 = Solution()
root = [5,2,10,1,3,8,13,None,None,None,4,None,None,11,15]
print(p1.preOrder(root))