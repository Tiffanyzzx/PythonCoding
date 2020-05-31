class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    def identicalBT(self, one, two):
        if not one and not two:
            return True
        if not one or not two:
            return False
        if one.val != two.val:
            return False
        return self.identicalBT(one.left, two.left) and self.identicalBT(one.right, two.right)