class Solution():
    def insert_numb(self, array, number):
        idx = len(array) - 1             # use idx to represent the last element of the inserted array
        array.append(number)             # this is where the number getting inserted into the array

        while idx >= 0:                  # base case is when idx < 0
            if array[idx] >= array[idx+1]:
                array[idx+1], array[idx] = array[idx], array[idx+1]
            else:
                break
            idx -= 1

    def inser_sort(self,array):
        new_list = []

        for i in range(len(array)):
            self.insert_numb(new_list,array[i])

        return new_list


# test

p1 = Solution()

a = [7,6,5,4,3,2,1]

res = p1.inser_sort(a)

print(res)