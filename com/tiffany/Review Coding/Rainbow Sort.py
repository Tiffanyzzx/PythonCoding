class Solution():
    def rainbow_sort(self, array):
        # three pointers
        left = 0
        index = 0
        right = len(array) - 1

        # Four regions:
        # [0, left) save -1
        # [left, index) save 0
        # [index, right] searching region
        # (right, len(array) - 1] save 1

        # use a while loop to check each element
        while index <= right:
            if array[index] == -1:
                array[index], array[left] = array[left], array[index]
                left += 1
                index += 1

            elif array[index] == 1:
                array[index], array[right] = array[right], array[index]
                right -= 1

            elif array[index] == 0:
                index += 1

        return array

a = [1,1,0,-1,0,1,-1]
p1 = Solution()
res = p1.rainbow_sort(a)
print(res)