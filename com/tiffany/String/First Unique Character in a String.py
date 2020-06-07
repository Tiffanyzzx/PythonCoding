class Solution(object):
    def firstUniqChar(self, input):
        """
        input: string input
        return: int
        """
        # two while loops
        # 1st: 以每个字母作为 keys, 以每个字母出现的次数作为 values
        # 2nd: 找出第一个且唯一出现一次的 character

        # 1st step
        # create a dict
        frequency = {}
        # iterate all elements containning in the input
        for c in input:
            # if the dict does not contain this character: key = character & value = 1
            if c not in frequency:
                frequency[c] = 1
            # if the dict already contains this character, then its value += 1
            else:
                frequency[c] += 1

        # 2nd step
        # iterate len(input) - 1 times depending on its index numbers
        for i in range(0, len(input)):
            # find the first non-repeating character & return its index
            if frequency[input[i]] == 1:
                return i
        # if does not exist, return -1
        return -1