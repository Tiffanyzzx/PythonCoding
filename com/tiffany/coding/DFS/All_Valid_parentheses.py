class Solution():
    def mainFunc(self,n):
        res, current = [], []
        left = 0
        right = 0
        if n <= 0:
            return "".join(res)
        self.helper(res, current, left, right,n)
        return res

    def helper(self, res, current, left, right, n):
        if left + right == 2 * n:
            res.append("".join(current))
            return
        if left < n:
            current.append("(")
            self.helper(res, current, left + 1, right, n)
            current.pop()
        if right < left:
            current.append(")")
            self.helper(res, current, left, right + 1, n)
            current.pop()

