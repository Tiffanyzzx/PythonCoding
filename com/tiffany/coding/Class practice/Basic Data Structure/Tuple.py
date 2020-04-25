# Tuple definition:
#     tuple is like a unchangeable list
#        - an ordered sequence of element, can mix element types
#        - cannot change element values, immutable
#        - represented with parentheses ()

# 1
# Tuple assignment
b = ("Tiffany", 27, "DS")  # tuple packing
(name, age, studies) = b
print(b)                   # Nothing happen
print(name)                # Tiffany
print(age)                 # 27
print(studies)             # DS

y = "-" * 50
print(y)



# 2
# iterate over tuples
nums = (1,2,3,4)
for num in nums:
    print(num)

y = "-" * 50
print(y)



# 3
# Other list operation
list = (2,4,1,6,6,6,4,9)
new_list = sorted(list)
print(new_list)

list.sort()
list.reverse()

y = "-" * 50
print(y)



