class Solution(object):
    def combinations(self, target, coins):
        """
        input: int target, int[] coins
        return: int[][]
        """
        combs, comb = [], []
        if not coins:
            return combs
        index = 0
        self.helper(combs, comb, index, target, coins)
        return combs

    def helper(self, combs, comb, index, target, coins):
        # base case
        if index == len(coins) - 1:
            if target % coins[index] == 0:
                comb.append(target / coins[index])
                combs.append(comb)
                comb.pop()
            return

        branches = target // coins[index]
        for num in range(0, branches + 1):
            comb.append(num)
            self.helper(combs, comb, index + 1, target - num * coins[index], coins)
            comb.pop()

p1 = Solution()
coins = {}