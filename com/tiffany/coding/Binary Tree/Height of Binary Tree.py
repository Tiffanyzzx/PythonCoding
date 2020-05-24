class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def height_of_BS(self, root):
        # base case : return zero is an important part, None level = 0 level
        if root is None:
            return 0

        # left child
        left = self.height_of_BS(root.left)
        # right child
        right = self.height_of_BS(root.right)

        # current level: + 1 is for current level
        curr = max(left, right) + 1

        # return
        return curr

p1 = Solution()
a= [1,2,7,3,None,None,None,4,None,5,None,6]
res = p1.height_of_BS(a)
print(res)