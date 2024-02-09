# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1:
#
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


# 思想：
# - 每个元素替换成该元素及之前数据的累加和
# - 当前元素往前k个元素平均值即为 (nums[idx] - nums[idx - k]) / float(k)
def process(nums, k):
    for idx in range(1, len(nums)):
        nums[idx] = nums[idx] + nums[idx - 1]
    res = nums[k - 1] / float(k)
    for idx in range(k, len(nums)):
        res = max(res, (nums[idx] - nums[idx - k]) / float(k))
    return res


if __name__ == '__main__':
    nums = [3, 3, 4, 3, 0]
    k = 3
    print(process(nums, k))
