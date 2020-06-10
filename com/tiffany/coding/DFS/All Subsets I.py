class Solution():
    def subSet(self, set):
        # create two lists for final res and current path
        res, current = [], []
        # corner case: Set = None, all the subsets are []
        # 这个 corner case不能写，不然input = "" 时会会return [] 而不是[""]
        # if not set:
        #     return res
        index = 0
        # set is a string,
        self.helper(res, current, set, index)
        return res

    def helper(self, res, current, set, index):
        # recursion base case
        # since 每一层只分 两叉，index == len(set) == leaf层数
        if index == len(set):
            res.append("".join(current))
        current.append(set[index])
        self.helper(res, current, set, index + 1)
        # 触底之后会触发 base case，回到上一层 current里到内容不变但是 index 会自动 - 1
        current.pop() # pop 之后 current里到内容会少了最后一个
        self.helper(res, current, set, index + 1)
