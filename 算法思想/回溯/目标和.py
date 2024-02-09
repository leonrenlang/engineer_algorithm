# 问题：
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
# 对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
# 示例：
# 输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 一共有5种方法让最终目标和为3。


# 回溯法
def ways_targetsum(nums, S):
    def backtrack(nums, i, remain):
        if i == len(nums):
            if remain == 0: res[0] += 1
            return
        backtrack(nums, i + 1, remain + nums[i])  # 选择列表中就两种选择，就不用循环，而是全部列出来
        backtrack(nums, i + 1, remain - nums[i])
    if len(nums) == 0: return 0
    res = [0]
    backtrack(nums, 0, S)
    return res[0]




# 动态规划(备忘录)
def ways_targetsum2(nums, target):
    def process(nums, i, remain):
        if i == len(nums):
            if remain == 0: return 1
            return 0
        key = str(i) + ',' + str(remain)
        if key in dic.keys():
            return dic[key]
        res = process(nums, i + 1, remain - nums[i]) + process(nums, i + 1, remain + nums[i])
        dic[key] = res
        return res
    if not nums: return 0
    dic = {}
    return process(nums, 0, target)


if __name__ == '__main__':
    nums = [6, 20, 22, 38, 11, 15, 22, 30, 0, 17, 34, 29, 7, 42, 46, 49, 30, 7, 14, 5]
    res = ways_targetsum(nums, 28)
    print(res)
