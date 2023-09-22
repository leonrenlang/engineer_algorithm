
# 最小的k的数字
# 思路1. 采用快排方法O(n)内找到第k个元素, 用快排partition划分，一直划中第k个数 最差情况o(kn)

class Solution:

    def partition(self, arr, first, last):
        pivot = arr[last]
        small = first
        for j in range(first, last):
            if arr[j] < pivot:
                arr[small], arr[j] = arr[j], arr[small]
                small += 1
        arr[small], arr[last] = arr[last], arr[small]
        return small

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 快速排序法：
        l = len(arr)
        if (l == 0) or (k>l):
            return
        if k == 0:
            return []
        if k == l:  # 不加此可能会有 bug
            return arr
        if l == 1:
            return arr

        left, right = 0, len(arr)-1
        while left <= right:   # 这里其实也相当于是二分法
            split_ind = self.partition(arr, left, right) # left, right, split_ind 都是原始 index
            if split_ind == k:   # 在 split_ind 左边有 k 个元素，全部不大于 pivot 
                break
            elif split_ind > k:
                right = split_ind-1  # 不-1 会陷入死循环
            else:
                left = split_ind+1  # 不 +1 会陷入死循环

        return arr[:k]


class Solution(object):
    def partition(self, arr, first, last):
        pivot = arr[last]
        small = first
        for j in range(first, last):
            if arr[j] < pivot:
                arr[small], arr[j] = arr[j], arr[small]
                small += 1
        arr[small], arr[last] = arr[last], arr[small]
        return small
    def getLeastNumbers(self, tinput, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        if k > len(tinput) or k <= 0: return []
        idx = self.partition(tinput, 0, len(tinput) - 1)
        low = 0
        high = len(tinput) - 1
        while idx != k - 1:
            if idx < k - 1:
                low = idx + 1
                idx = self.partition(tinput, low, high)
            if idx > k - 1:
                high = idx - 1
                idx = self.partition(tinput, low, high)
        return tinput[:k]

