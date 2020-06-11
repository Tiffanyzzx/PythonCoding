class Solution(object):
    def permutations(self, input):
        """
        input: string input
        return: string[]
        """
        perms = []
        if not input:
            return perms.append("")
        index = 0
        set_list = list(input)
        self.helper(perms, index, set_list)
        return perms

    def helper(self, perms, index, set_list):
        if index == len(set_list):
            perms.append("".join(set_list))
            return
            # for loop represents 叉数会每一层减少
        for i in range(index, len(set_list)):
            # 吃
            set_list[i], set_list[index] = set_list[index], set_list[i]
            self.helper(perms, index + 1, set_list)
            # 吐
            set_list[i], set_list[index] = set_list[index], set_list[i]


