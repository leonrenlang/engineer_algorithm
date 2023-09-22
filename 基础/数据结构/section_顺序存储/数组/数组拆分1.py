#
# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
# 示例 1:
# 输入: [1,4,3,2]
# 输出: 4
# 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
# 提示:
# n 是正整数,范围在 [1, 10000].
# 数组中的元素范围在 [-10000, 10000].


# 思路1：贪心
# - 我们希望每队数相差最小，因此每对数的值应该非常接近
# 排序后依次选取数据，每对数据的值就非常接近
# - 时间O(nlogn),空间(O(n))
def process(nums):
    nums.sort()
    i = 0
    res = 0
    while i < len(nums):
        res += nums[i]
        i += 2
    return res


# 思路2：
# - 由于数据的范围已经，可以用计数排序简化时间复杂度
def process2(nums):
    arr = [0] * 20001
    for num in nums:
        arr[num + 10000] += 1

    nums_sorted = []
    for idx in range(len(arr)):
        nums_sorted += [idx - 10000] * arr[idx]
    i = 0
    res = 0
    while i < len(nums_sorted):
        res += nums_sorted[i]
        i += 2
    return res
