# Definition:
# 1) Variable (reference) & the value of the variable (object) are different, they are two separated things!
# 2) The variable is NOT the object

x = []
# [ ] is the empty list, x is the variable that points the empty list, but x itself it NOT the empty list
# Consider the variable (x) as a box, and the value of the variable ([ ]) as the object inside the box


# Example 1 : reassignment
x = [0]
y = x
y = [1]
print(x)  # x is [0]
print(y)  # y is [1]

y = "-" * 50
print(y)



# Example 2 : Modify
x = [0]
y = x
y[0] = 1
print(x)  # x is modified by y[0] = 1, so x is [1]
print(y)  # y is [1]

y = "-" * 50
print(y)



# 3) A function receives a reference to the same object in the memory as used by the caller.
#  the function provides its own box and creats a new variable for itself

# Example 3 : Function $ Reassign & Modify

# 3.1 reassign
def reassign(x):
    x = [1]     # the copied x pointing to another object


x = [0]         # assign x equal to 0
reassign(x)     # use the function, open a copied variable pointing to [0] but reassigned to [1] after reading the function
print(x)        # this x print [0], does not get impacted by the reassign function

y = "-" * 50
print(y)



# 3.2 reassign

def reassign(x):
    x = [1]    # the copied x pointing to another object
    print(x)   # including a x in the function, x = 1

x = [0]
reassign(x)    # use the function, open a copied variable pointing to [0] but reassigned to [1] after reading the function
print(x)       # this x print [0], does not get impacted by the reassign function

y = "-" * 50
print(y)



# 3.3 Modify

def modify(x):
    x[0] = 1   # the copied x is getting modified to change to another value

x = [0]        # original x is pointing to [0] object
modify(x)      # create a copied x pointing to the original object, but the object will get modified after reading the method
print(x)       # x = 1

y = "-" * 50
print(y)

# 3.4 modify

def changeme(mylist):
    mylist.append([1,2,3])
    return

mylist = [10, 20, 30]
changeme(mylist)
print("value outside of the function:", mylist)











