import math

#  Example 1:
#  Prime Number: a number with exactly 2 factors ( 1 & itself ). 1 is not a prime number.
#  The way to check whether one number divides another is to use % operation.

def isPrime(x):
    if x == 1:
        return False
    for i in range (2, x):
        if x % i == 0:        # modulus = 0 means x could be divided by a third factor
            return False
    return True



# Example 2:
# Composite number: a number with more than 2 factors (opposite of prime number)

# 2.1 composite number version one
def isComposite_v1(x):
    if x == 1:
        return False
    for i in range (2, x):
        if x % i == 0:
            return True
    return False

# 2.2 composite number version two
def isComposite_v2(x):
    if x == 1:
        return False
    return not isPrime(x)


# Example 3:
# Perfect number: a number is said to be perfect if it is equal to the sum of all its factors.
# ( 6 = 3+2+1, hence 6 is perfect; 28 = 1+2+4+7+14 )

# 3.1 find the sum of all x's factor
def factorSum(x):
    sum_of_factor = 0
    for i in range (1, x):
        if x % i == 0:
            sum_of_factor += 1
    return sum_of_factor

# 3.2 check whether number x is perfect
def isPerfec(x):
    return factorSum(x) == x 


# Example 4:
# Abundant number: a number is considered to be abundant if the sum of its divisors is greater than the number itself.
# ( 12 is abundant since 1+2+3+4+6 = 16 > 12)


# Example 5:
# a number that can be expressed in the form (n + 1)*(n/2)

# Hexagonal number
# a number that can be expressed in the form 2n^2 - n