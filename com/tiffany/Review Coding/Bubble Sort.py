class Solution():
    def bubble_sort(self, list):

        for i in range(len(list)-1, 0, -1):    # from the last index to 1, zero is not included
            print("level ", i)

            for j in range(i):                 # from zero to the second last index, the last index is not included
                print("compare ", j)

                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
                    print("after swap ", list)

p1 = Solution()

a = [9,8,7,6,5,4,3]

res = p1.bubble_sort(a)

print(res)


# time complexity O(n^2)
# space complexity O(1)