# 总结： 二分查找的各个用法
# 1. 找到返回其索引，没找到返回-1        -- 基础写法


# 2. 找到返回，如果有重复返回其左边界      -- binary_search_left_bound
# 3. 找到返回，如果有重复返回其右边界      -- binary_search_right_bound

# 4. 返回应该在哪里插入target的索引i, 要求a[:i]中的元素都小于target, a[i:]中的元素大于等于target
# 所以如果target已经在数组中了，会插入最左边的target前面
# -- bisect_left == binary_search_left_bound
# 5. 返回应该在哪里插入target的索引i, 要求a[:i]中的元素都小于等于target, a[i:]中的元素大于target
# 所以如果target已经在数组中了，会插入最右边的target的右边
# -- bisect_right = binary_search_right_bound() + 1
# 注：两者的唯一区别是当target存在的时候，一个范围最左边的target的index,一个返回最右边的target的右边


# 基础写法：basic way
def binary_search(lis, target):
    i = 0
    j = len(lis) - 1
    while i <= j:
        mid = (i + j) // 2
        if lis[mid] > target:
            j = mid - 1
        elif lis[mid] < target:
            i = mid + 1
        elif lis[mid] == target:
            return mid
    return -1
    # print('i:', i)  # 二分查找如果没找到i一定等于j+1,j和i分别代表aim所在位置的左边和右边
    # print('j:', j)  # 但是如果aim值小于最小值，j就会等于-1，aim如果大于最大值，i就会等于len(arr)，索引就超出了范围


# 寻找左侧边界的二分搜索:
# - 返回值可以理解为nums中小于target的元素有多少个,返回结果的范围[0, len(nums)]
# - while中为什么是 < 不是 <= ?
# 对于搜索左右边界的二分查找，这种写法比较普遍
# - 这种方法并不知道是否找到了目标元素，如果要进行判断可以增加代码
# if left == len(nums) return -1
# return left if nums[left] == target else -1
# - 为什么边界的变化是left = mid + 1, right = mid?
# 因为搜索区间是[left, right)左闭右开，所以当nums[mid]被检测之后，下一部分是搜索区间
# 应该去掉mid分割成两个区间即，[left, mid)或[mid+1, right)
def binary_search_left_bound(nums, target):
    if len(nums) == 0: return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            right = mid  # 这里是关键，即使找到了目标值，也不立即停止，因为目标值可能有重复，找最左边一个
    return left  # 返回left或者right都可以，因为停止条件是left = right


# 寻找右侧边界的二分查找:
# - 返回结果范围是[-1, len(nums)-1],
# 当target存在时可以理解为寻找最右边的target，
# 当target不存在时可以理解为要将目标值放入数组中，从右往左依次查找，直到找到第一个<=自己的，
# 返回其索引，覆盖掉
def binary_search_right_bound(nums, target):
    if len(nums) == 0: return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            left = mid + 1
    return left - 1  # python 官方的bisect_right是直接返回left


# 返回应该在哪里插入target的索引i, 要求a[:i]中的元素都小于target, a[i:]中的元素大于等于target
# 所以如果target已经在数组中了，会插入最左边的target前面
# -- bisect_left == binary_search_left_bound
def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# 返回应该在哪里插入target的索引i, 要求a[:i]中的元素都小于等于target, a[i:]中的元素大于target
# 所以如果target已经在数组中了，会插入最右边的target的右边
# -- bisect_right = binary_search_right_bound() + 1
def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == '__main__':
    lis = [1, 3, 5, 5, 5, 5, 7, 9]
    aim = 3
    for aim in range(0, 13):
        print('aim:', aim)
        # print(binary_find(lis, aim))
        # print(binary_search_left_bound(lis, aim))
        print(binary_search_right_bound(lis, aim))
        print('-' * 50)
