# 数组的全排列问题：输出给定数组的所有全排列


# 思想：
# - 回溯法
# - 决策树的第一层的选择列表是数组中的所有元素
# - 将某一个元素加入到路径中，对其进行backtrack, 子问题的其选择列表是除了该元素的所有元素
# - 终止条件是当路径的长度与数组的长度相等
def permutation(nums):
    def backtrack(nums, track):
        if len(track) == len(nums):
            res.append(track[:])
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])  # 同时将选择从选择列表移除以及将选择加入到路径中
            backtrack(nums, track)
            track.remove(nums[i])

    res = []
    backtrack(nums, [])
    return res

def permutation(nums):
    
    def backtrack(nums, track):
        if len(track) == len(nums):
            res.append(track[:])
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            backtrack(nums, track)
            track.remove(nums[i])
    res = []
    

if __name__ == '__main__':
    arr = [1, 2, 3]
    print(permutation(arr))
