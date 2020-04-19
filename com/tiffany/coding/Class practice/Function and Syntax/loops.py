# Question # 1
count = 0
while count < 10:
    print("The count is: ", count)
    count += 1

y = "-" * 50
print(y)



# Question # 2
count = 0
while count < 10:
    count += 1
    print("The count is: ", count)

y = "-" * 50
print(y)




# Question # 3

# Question # 3.1
for letter in "laioffer":
    print("letter is", letter)

y = "-" * 50
print(y)

# Question # 3.2
for letter in "laioffer":
    if letter == "i":
        break
    print(letter)

y = "-" * 50
print(y)

# Question # 3.3
for letter in "laioffer":
    if letter == "i":
        continue
    print(letter)

y = "-" * 50
print(y)




# Question # 4
names = ["Tiff", "Andy", "Gab"]
for name in names:
    print(name)

y = "-" * 50
print(y)




# Question # 5

# Question # 5.1
for i in range(1,3):
    print(i)

y = "-" * 50
print(y)

# Question # 5.2
for i in range(1, 3):
    for letter in "laioffer":
        if letter == "i":
            break
        print("letter is", letter)
    print(i)

y = "-" * 50
print(y)

# Question # 5.3
for i in range(1, 3):
    for letter in "laioffer":
        if letter == "i":
            continue
        print("letter is", letter)
    print(i)

y = "-" * 50
print(y)





# Question # 6

# Question # 6.1
sum = 0
for i in range(3):  # it means [0,3)
    print(i)
    sum += 5
print(sum)

y = "-" * 50
print(y)

# Question # 6.2
total = 0
for i in range(1, 5):  # it means 1 & 2
    print(i)
    total += 5
print(total)

y = "-" * 50
print(y)

# Question # 6.3
nums = 0
for i in range(0, 10, 2):  # 2 means 0, 2, 4, 6, 8 but not include 10
    print(i)
    nums += 5
print(nums)

y = "-" * 50
print(y)




# Question # 7

# Question # 7.1
sum = 0
for i in range(3):  # repeat three times
    sum += int(input("Insert number:"))  # type int as type, insert three numbers and sum them up
print(sum)

y = "-" * 50
print(y)

# Question # 7.2
total = 0
n = int(input("How many numbers you would like to add: "))
for i in range(n):
    total += int(input("Insert numbers: "))
print(total)