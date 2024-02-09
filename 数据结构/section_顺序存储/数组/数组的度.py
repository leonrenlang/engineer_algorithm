# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
# 示例 1:
#
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 示例 2:
#
# 输入: [1,2,2,3,1,4,2]
# 输出: 6


# 思想：
# - 若已知数组的度，且知道具体的某一个元素，那么最大连续子数组一定是以该具体元素开头和结尾的
# - 比较所有满足条件的元素
def process(nums):
    left, right, count = {}, {}, {}
    for i, item in enumerate(nums):
        if item not in left.keys():
            left[item] = i
        right[item] = i
        count[item] = count.get(item, 0) + i
    ans = len(nums)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x]-left[x] + 1)
    return ans
