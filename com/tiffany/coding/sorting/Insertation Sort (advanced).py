class Solution():
    def insert_sort(self, array):
        for i in range(1, len(array)):    # start from index 1 is bcuz of the following while loop, [k-1]
            curr = array[i]               # save current array[i] using curr variable
            k = i                         # using k to copy the index of i


            while k > 0 and curr < array[k-1]:
                array[k] = array[k-1]
                k -= 1

            array[k] = curr


p1 = Solution()

a = [3,2,6,4,5,9,1]

res = p1.insert_sort(a)

print(a)