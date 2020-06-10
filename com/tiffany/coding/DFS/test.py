def perm(self, set):
    res = []
    set_list = list(set)
    index = 0
    self.helper(res, set_list, index)
    if len(res) == 0:
        res.append("")
        return res


def helper(self, res, set_list, index):
    if index == len(set_list) - 1:
        res.append(" ".join(set_list))
        return res
    for i in range(index, len(set_list)):
        set_list[index], set_list[i] = set_list[i], set_list[index]
        self.helper(res, set_list, index + 1)
        set_list[index], set_list[i] = set_list[i], set_list[index]

set = ["abc"]
print(perm(set))
