class Solution():
    def bubble_sort(self, list):
        for i in range(len(list)-1, 0, -1):
            for j in range(i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
        return list

p1 = Solution()
a = [3,1,5,8,3,10]
res = p1.bubble_sort(a)
print(res)


# time complexity is O(n)
