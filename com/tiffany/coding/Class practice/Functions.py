# function grammar:
# def function_name(parameter1, parameter2):
#       statement 1
#       statement 2
#       return[expression]   #if there does not have a return value, then you do not need to write return


# Question # 1
# required arguments
def printme(str):
    print(str)
    return

print("Allen")

y = "-" * 50
print(y)





# Question # 2
# keyword arguments

# 2.1 print as default order
def printinfo_1(name, age):
    print("Your name is ", name)
    print("Your age is ", age)
    return

printinfo_1("Tiffany", 26)

y = "-" * 50
print(y)


# 2.2 print using keyword, could be disorder
def printinfo_2(name, age):
    print("Your name is ", name)
    print("Your age is ", age)
    # not writing a return also works

printinfo_2(age = 24, name = "Wen")

y = "-" * 50
print(y)


# 2.3 parameter could be assigned at the beginning
def printinfo_3(name, age = 23):
    print("Your name is", name)
    print("Your age is", age)
    return

printinfo_3(name = "Andy") # you do not need to write two arguments becuz the age was assigned at the beginning

printinfo_3(name = "Haofei", age = 35) # age is also changeable

y = "-" * 50
print(y)




# Question # 3
# Global vs. Local variable

y = "-" * 50
print(y)


# Question # 1
# required arguments

y = "-" * 50
print(y)


# Question # 1
# required arguments

y = "-" * 50
print(y)


# Question # 1
# required arguments

y = "-" * 50
print(y)