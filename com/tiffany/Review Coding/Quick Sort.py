class Solution():
    # alist is a given array, left = 0 and right = len(array) - 1
    def partition(self, alist, left, right):

        import random
        # randomly pick a index between left and right
        rand = random.randint(left, right)

        # exchange the randint with right spot (index)
        alist[rand], alist[right] = alist[right], alist[rand]

        # use pivot to represent the value containing in right index, which is the randint
        pivot = alist[right]

        # using start and end as two pointers in the while loop to iterate each element except pivot
        # two pointer with one pivot (pivot = alist[right])
        # three regions
        # [0, start)  < pivot
        # [start, end] searching area
        # (end, right - 1) > pivot
        start = left
        end = right - 1
        while start <= end:
            if alist[start] < pivot:
                start += 1
            elif alist[end] >= pivot:
                end -= 1
            # elif: alist[start] >= pivot and alist[end] < pivot
            else:
                alist[start], alist[end] = alist[end], alist[start]
                start += 1
                end -= 1
        # start > end, above while loop stopped
        alist[start], alist[right] = alist[right], alist[start]

        return start

    def quick_sort(self, alist, left, right):

        # base case for following recursion
        if left >= right:
            return


        pivot = self.partition(alist, left, right)
        self.quick_sort(alist, left, pivot - 1)
        self.quick_sort(alist, pivot + 1, right)

    def quickSort(self,array):

        # identify alist, left and right
        self.quick_sort(array, 0, len(array) - 1)

        return array


a = [5,2,1,4,3]
p1 = Solution()
res = p1.quickSort(a)
print(res)
