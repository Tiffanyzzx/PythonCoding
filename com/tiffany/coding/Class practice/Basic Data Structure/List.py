# ordered sequence of info, accessible by index
# a list is denoted by square bracket, [ ]
# can contain mixed types elements
# changeable
# mutable, assign an element at an index changes the value

# 1
lst = [1,2,3,4,5]
print(lst)        # lst = [1, 2, 3, 4, 5]

lst.append(2)     # adding a element at the end of the list
print(lst)        # lst = [1, 2, 3, 4, 5, 2]

y = "-" * 50
print(y)





# 2
# iterate on list
lst = [1,2,3,4,5]
for x in lst:
    print(x)

y = "-" * 50
print(y)

# iterate on list & compute the sum of elements of a list
a = [1,2,3]
b = [4,5,6]
res = []         # create a blank list

                 # a & b have to have same lengthes to be able to sum up
for i in range(len(a)):
    res.append(a[i] + b[i])
print(res)       # list = [5, 7, 9]

y = "-" * 50
print(y)




# 3
# add ONE element to the end of list (mutates the list)
L = [1,2,3]
L.append(4)
print(L)        # L = [1, 2, 3, 4]
L.append(" Hi ")
print(L)        # L = [1, 2, 3, 4, ' Hi ']

y = "-" * 50
print(y)

# using + to combine lists together
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print(L3)

y = "-" * 50
print(y)

# adding MORE than one element ( add a list)
L1 = [1,2,3]
L1.extend([10, 20, 30])
print(L1)      # L1 = [1, 2, 3, 10, 20, 30]

y = "-" * 50
print(y)


# 4
# Delete element

# delete a specific index with del(L[index])
L = [1, 1, 2, 2, 3, 3, 4]
del(L[0])
print(L)       # L = [1, 2, 2, 3, 3, 4]

y = "-" * 50
print(y)

# Remove an element at the end of a list with L.pop()
L = [1, 1, 2, 2, 3, 3, 4]
L.pop()
print(L)       # L = [1, 1, 2, 2, 3, 3]

y = "-" * 50
print(y)

# Remove a specific element (by value) with L.remover(element)
#       if it is a repeated elements, remove the FIRST occurrence
#       if element is not in the list, give an ERROR
L = [1, 1, 2, 2, 3, 3, 4]
L.remove(2)
print(L)      # L = [1, 1, 2, 3, 3, 4]

y = "-" * 50
print(y)


L = [1, 1, 2, 2, 3, 3, 4]
L.remove(5)   # ValueError: list.remove(x): x not in list














