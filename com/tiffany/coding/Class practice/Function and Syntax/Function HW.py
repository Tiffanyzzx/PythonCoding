# 1
def foo1(x):
    x.append(1)
    x = [2]
    x.append(1)
    print("Inside x is:", x)

x = [0]
foo1(x)
print("Outside x is: ", x)

y = "-" * 50
print(y)



# 2
def foo2(x):
    x.append(1)
    x.append(2)
    x = [2]
    print("Inside x is:", x)

x = [0]
foo2(x)
print("Outside x is:", x)

y = "-" * 50
print(y)



# 3
def foo3(x):
    x = [2]
    x.append(1)
    x.append(2)
    print("Inside x : ", x)

x = [0]
foo3(x)
print("Outside x: ", x)


