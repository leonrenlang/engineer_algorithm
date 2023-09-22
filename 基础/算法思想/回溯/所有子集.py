# 数组的所有子集问题：输入一个不包含重复数字的数组，要求算法输出这些数字的所有子集


# 思想1：
# - 普通递归法
# - 获取前n-1个数的所有子集，将每个子集append()第n个数生成新的子集，将n-1的子集和新的子集
# 合并，即为规模为n的解
# - base case, 当数组长度为0时，仅有一个子集，为[]
def subsets(nums):
    if len(nums) == 0:
        return [[]]
    res = subsets(nums[:-1])
    new_res = []
    for item in res:
        new_res.append(item)
        new_item = item + [nums[-1]]
        new_res.append(new_item)
    res = new_res
    return res


# 思想2：
# - 回溯法，其遍历思想与将每个元素看作可以出现和不可以出现的思想不同
# - 决策树的第一层，认为所有的元素都在选择列表中
# - 将某一个元素加入到路径中，对其进行backtrack, 在这里要注意的是
# 对于每个元素的backtrack，其后的选择列表是源数组中跟在该元素之后的元素，而不是
# 除了该元素外的所有元素。
# - 为了遍历当前的选择列表，对该元素backtrack后，需要将其从路径中去除，以对选择列表
# 中的其他元素进行回溯。

# 这种回溯写法相比下面那种更符合直觉
# - 选择列表：对于每一个元素，可以选择要或者不要
# - 结束条件：索引到达了最后一个
def subsets3(nums):
    def backtrack(nums, i, track):
        if i == len(nums):
            res.append(track[:])
            return
        track.append(nums[i])
        backtrack(nums, i + 1, track)
        track.remove(nums[i])
        # 选择不要就不用修改路径
        backtrack(nums, i + 1, track)
    res = []
    backtrack(nums, 0, [])
    return res


def subsets2(nums):
    def backtrack(nums, start, track):
        res.append(track[:])
        for i in range(start, len(nums)):
            track.append(nums[i])
            backtrack(nums, i + 1, track)  # 选择了一个元素之后，只能继续回溯该元素之后的数字
            track.remove(nums[i])

    res = []
    backtrack(nums, 0, [])
    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 5]
    res = subsets3(nums)
    print(res)
    print(len(res))
