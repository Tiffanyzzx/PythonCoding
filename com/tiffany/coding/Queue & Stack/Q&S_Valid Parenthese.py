class Solution():
    def isValid(self, input):
        s = []
        match = {'(': ')', '[': ']', '{': '}'}

        for x in input:
            if x in match:
                s.append(x)
            elif s and match[s[-1]] == x:
                s.pop()
            elif not s or match[s[-1]] != x:
                return False

        return not s


p1 = Solution()
a = ["{", "[", "(", ")", "]", "}"]
res = p1.isValid(a)
print(res)