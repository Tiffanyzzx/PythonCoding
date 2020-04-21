# String

# 1
# grammar: quotation marks or single quotes
a = "i phone"            # save as an list in hard drive, memory: ["i", " ", "p", "h", "o", "n", "e"]
b = 'i phone'
c = '''i phone'''
d = """i phone"""
print(a)
print(b)
print(c)
print(d)

y = "-" * 50
print(y)



# 2
# Concatenate strings (combine two strings into one)
a = "Hello "
b = "my bro"

combine = a + b
print(combine)            # combine = "Hello my bro"

y = "-" * 50
print(y)




# 3
# Operation (*)
a = "Hello"
b = "my bro"
c = a + " " + b * 3
print(c)                 # Hello my bromy bromy bro

y = "-" * 50
print(y)



# 4
# Compare strings with ==, <, >, etc
print("derea" < "derek") # True, the main point is comparing letter "a" and "k"
print("a" < "k")         # True, k is bigger than a

print("Derek" < "derek") # True, the main pt is the 1st letter
print("D" < "d")         # lower case is bigger than upper case

print("greeting" < "derek") # False, g is bigger than d, ordering by 24 english letters
print("g" < "derek")        # False, length of "greeting" is longger than "derek" but it does NOT matter

y = "-" * 50
print(y)



# 5
# length of a string
a = "abc"
print(len(a))            # the length is 3

y = "-" * 50
print(y)



# 6
# String can NOT be modified & String is immutable
a = "hello"
print(a[0])              # output is h, string is extractable
# a[0] = "y"               # gives an error, string can NOT be modified. String is immutable

# a = "y" + a[1:len(0)]    # is allowed, a bound to a new object

y = "-" * 50
print(y)



# 7
# iterate
s = "abcdefg"
for x in s:
    print(x)

y = "-" * 50
print(y)

s = "abcdefg"
for i in range(4):
    print(i)
    print(s[i])

y = "-" * 50
print(y)

s = "abcdefg"
for i in range(2,5):
    print(i)
    print(s[i])

y = "-" * 50
print(y)

s = "abcdefg"
for i in range(0, len(s), 2):
    print(i)
    print(s[i])














