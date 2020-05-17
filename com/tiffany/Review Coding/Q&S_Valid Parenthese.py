# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. The brackets must close in the correct order.
#
# Examples
#
# "()" and "()[]{}", "[{()}()]" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, input):
        """
        input: string input
        return: boolean
        """
        # write your solution here
        # stack
        s = []
        # dic to look up key & value pair, <left, right>
        match = {'(': ')', '{': '}', '[': ']'}
        # iterate the input array
        for x in input:
            # if x is one of the keys containing in the match dict
            if x in match:
                # if yes, append x into the stack container (s)
                s.append(x)
            # if not s 是 it is when s == None or len(s) == 0 的简写: 特制当input是空时或者input里的第一个不是key时没办法append进去stack            # if match[s[-1]] != x:
            # s[-1] 指的是 stack container (s) 里最上面的那一个
            # 首先 stack 里的肯定都是 dictionary 里的 keys，那么 match[s[-1]] 是用key back to dictionary里去找它对应的value
            # match[s[-1]] != x ，如果这两个 values 不匹配，那就return false
            elif not s or match[s[-1]] != x:
                return False
            # 如果match上了，那就把stack里的key消除掉
            else:
                s.pop()

        # when s is empty, [], None, or len(s) == 0
        # return True
        return not s


p1 = Solution()
a = ["{", "[", "(", ")", "]", "}"]
res = p1.isValid(a)
print(res)
