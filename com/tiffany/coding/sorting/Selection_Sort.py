# Question: Given an array of integers, sort the elements in the array in ascending order.
# The selection sort algorithm should be used to solve this problem.

# Examples
# {1} is sorted to {1}
# {1, 2, 3} is sorted to {1, 2, 3}
# {3, 2, 1} is sorted to {1, 2, 3}
# {4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}

# Corner Cases
# What if the given array is null? In this case, we do not need to do anything.
# What if the given array is of length zero? In this case, we do not need to do anything.


class Solution():
    def selection_sort(self, list):
        for i in range(0, len(list)):
            print("level ", i)

            min = i

            for j in range(i, len(list)):
                print("compare", j)
                if list[j] < list[min]:
                    min = j
                    print("min aft compare ", min)

            list[i], list[min] = list[min], list[i]
            print("after swag", list)

        return list


p1 = Solution()

a = [9,8,7,1,2,3]

res = p1.selection_sort(a)

print(res)





# Solution one: from max to min
class Solution1():
    def solve(self, array):
        # step 1: for loop checking
        # 1.1: checking from the end of the array to the beginning of the array
        for i in range(len(array) - 1, 0, -1):
            max = i
            #1.2: nested loop, compare with item contained in the array to look for max#
            for j in range(0, i+1): # does not include i + 1, end at i
                if array[j] > array[max]:
                    max = j
            # step 2: swap
            array[i], array[max] = array[max], array[i]

        # step 3: print our sorted array
        return array

p1 = Solution1()
array = [3,5,1,2,4,8]
res = p1.solve(array)
print(res)

# Solution two: from min to max
class Solution2():
    def solve2(self, array):
        for i in range(0, len(array), 1): # important
            min = i
            for j in range (i, len(array)): # important
                if array[j] < array [min]:
                    min = j
            array[i], array[min] = array[min], array[i]
        return array
p2 = Solution2
array2 = [3,5,1,2,4,8]
res = p2.solve2(array)
print(res)
