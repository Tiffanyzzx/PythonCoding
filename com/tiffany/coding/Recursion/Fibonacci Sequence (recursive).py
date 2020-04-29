# Get the Kth number in the Fibonacci Sequence. (K is 0-indexed, the 0th Fibonacci number is 0 and the 1st Fibonacci number is 1).

# Examples
# 0th fibonacci number is 0
# 1st fibonacci number is 1
# 2nd fibonacci number is 1
# 3rd fibonacci number is 2
# 6th fibonacci number is 8

class Solution():

    def fib(self, n):

        if n < 0:
            return 0

        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)

