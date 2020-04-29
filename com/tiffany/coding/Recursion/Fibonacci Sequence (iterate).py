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
            return n       # in fib seq, n is equal to zero and one for the first and second fib numbers, respectively

        num_a = 0          # use num_a to represent the first numb of fib seq
        num_b = 1          # use num_b to represent the second numb of fib seq

        for i in range(n-1):  # (n-1) it's bcuz numb_a/b have represented the 1st&2nd fib numbers
            temp = num_b   # use temp to save the object num_b is pointing to
            num_b += num_a # num_b = num_b + num_a = array(n-1) + array(n-2), this is the numb gonna be returned
            num_a = temp   # this is like a swag

        return num_b

