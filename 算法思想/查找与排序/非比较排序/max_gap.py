
# 用了桶的思想，但是是基于比较的排序

# 给定一个数组，求如果排序之后，相邻两数的最大差值，要求时间复杂度O(N)，
# 且要求不能用非基于比较的排序。
# 注：其实这个题目是有意义的，如果是浮点数对象，就没法用计数排序
#       如果数据是自定义对象，就不能用非基于比较排序的方法实现

# 思想：
# 1.  如果有N个数，那准备N+1个桶，遍历，找到最小值和最大值
# - 如果最大最小值的差值为0，则最大差值为0
# 2. 否则，将[mini,maxi]范围等分为(N+1)份，把每个对象放入对应的桶里
# 3. 根据鸽笼原理，一定存在一个空桶，那么最大差值一定不会出现在同一个桶中
# - 对于每个桶，仅需保留其最大最小值，和一个bool类型，桶内是否有值
# - 遍历桶，找每个非空桶左边离其最近的非空桶的最大值与其最小值的差值
# 注：此方法是基于比较的


def max_gap(nums):

    def bucket_idx(num, length, mini, maxi):
        # 返回num应该属于哪个桶内
        return int((num - mini) * length / (maxi - mini))

    if len(nums) < 2:
        return 0

    mini = nums[0]                               # 获取最大/小值
    maxi = nums[0]
    for item in nums:
        if item > maxi: maxi = item
        if item < mini: mini = item
    if mini == maxi: return 0

    length = len(nums)                          # 初始化length+1个桶
    has_num = [0] * (length+1)
    mins = [0] * (length+1)
    maxs = [0] * (length+1)
          
    for i in range(len(nums)):                           # 入桶
        bid = bucket_idx(nums[i], length, mini, maxi)
        mins[bid] = nums[i] if has_num[bid] == False else min(nums[i], mins[bid])
        maxs[bid] = nums[i] if has_num[bid] == False else max(nums[i], maxs[bid])
        has_num[bid] = True
    
    res = 0                                #遍历桶，找到差值最大的
    last_max = maxs[0]
    for i in range(1, len(nums)+1):
        if has_num[i]:
            res = max(res, mins[i] - last_max)
            last_max = maxs[i]
    return res

if __name__ == "__main__":
    lis = [12,2,4,4,4,24,24,4,21,2,456465]
    print(max_gap(lis))
