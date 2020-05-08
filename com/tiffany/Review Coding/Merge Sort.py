class Solution():
    def merge_sort(self, array):
        # corner case checking for following recursion
        if len(array) <= 1:
            return array

        mid = len(array) // 2                          # cut an array into two parts

        # these recursions are gonna continue cutting each array into two parts
        left_half = self.merge_sort(array[:mid])       # not include the mid
        right_half = self.merge_sort(array[mid:])      # include the last element by default

        # after cutting, there will only be single element remained
        # use another recursion to merge these single element back to a sorted array
        return self.merge(left_half,right_half)

    def merge(self, left_half, right_half):
        # set i for left & j for right
        i = 0
        j = 0
        # create a new list for sorted elements
        alist = []

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                alist.append(left_half[i])
                i += 1

            elif left_half[i] > right_half[j]:
                alist.append(right_half[j])
                j += 1

        # do a post processing if one of the array is gone
        while i < len(left_half):
            alist.append(left_half[i])
            i += 1

        while j < len(right_half):
            alist.append((right_half[j]))
            j += 1

        return alist

a = [2,3,1,4,6,5,7]
p1 = Solution()
res = p1.merge_sort(a)
print(res)

