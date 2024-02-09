# 找出数组中重复的数字。

# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
# 请找出数组中任意一个重复的数字。
# 示例 1：
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3


# 思想：
# 遍历数组 nums ，设索引初始值为 i = 0:
# -若 nums[i] == i ： 说明此数字已在对应索引位置，无需交换，因此执行 i += 1 与 continue ；
# -若 nums[nums[i]] == nums[i] ： 说明索引 nums[i] 处的元素值也为 nums[i]，即找到一组相同值，返回此值 nums[i]；
# 否则： 当前数字是第一次遇到，因此交换索引为 i 和 nums[i] 的元素值，将此数字交换至对应索引位置。
# -若遍历完毕尚未返回，则返回 −1 ，代表数组中无相同值。


def process(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
        elif nums[nums[i]] == nums[i]:
            return nums[i]
        elif nums[nums[i]] != nums[i]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    res = process(nums)
    print(res)
