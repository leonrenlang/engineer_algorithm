# 问题：给定一个无序的整数数组，找到其中最长上升子序列的长度。


# 思路1：动态规划
# - 规模为n的问题定义为以第n个数为结果的最大上升子序列的长度（注意和原问题不同）
# - 大问题与小问题之间的关系：f(n)等于max(g(f(n-1)), g(f(n-2)), ....)
# 其中g()代表，如果数列的第n个数大于子问题对应的最后一个数，那么结果等
# 于max(子问题的结果+1),否则就等于子问题的最大值
# - base case: 数组长度为1，结果为1
# - 时间复杂度为O(n2)
def length_of_incre_subseq(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# 思路2：贪心+二分
# - 在使用dp的时候计算每个dp值，都需要遍历前面的所有子问题，进行判断，
# 如果前面的子问题是有序的，那么就可以用二分查找遍历，时间复杂度就变为O(nlogn)
# - 准备一个辅助数组，辅助数组中保存当前最优的最长子序列
# - 遍历源数组，根据当前元素的值更新最长子序列，找到最长子序列中大于或等于当前元素的第一个元素，
# 用当前元素覆盖它，如果找不到，则将当前元素附在最长子序列的末尾。（寻找过程用二分查找的变体）
def length_of_incre_subseq2(nums):
    tails, res = [0] * len(nums), 0  # res直接tails数组的最后一个值的右边
    for num in nums:
        i, j = 0, res
        while i < j:  # 这种二分方式保证最后i所在的位置大于等于目标值，但不用担心数组不够装问题的，因为辅助数组的大小和源数组大小相同
            m = (i + j) // 2
            if tails[m] < num:
                i = m + 1
            else:
                j = m
        tails[i] = num  # 将num赋予i
        if j == res:
            res += 1
    return res


def length_of_incre_subseq3(nums):
    import bisect
    inc_subseq = [0] * len(nums)
    res = 0
    for item in nums:
        # 当不允许重复值出现，bisect_left,否则bisect_right
        index = bisect.bisect_left(inc_subseq, item, 0, res)
        inc_subseq[index] = item
        if index == res:
            res += 1
    return res


if __name__ == '__main__':
    arr = [4, 10, 4, 3, 8, 9]
    print(length_of_incre_subseq2(arr))
    print(length_of_incre_subseq3(arr))
