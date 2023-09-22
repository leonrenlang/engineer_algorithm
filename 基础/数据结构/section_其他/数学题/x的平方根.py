# 思想：二分查找
# - 时间O(logn)， 空间O(1)
def my_sqrt(x):
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (1 + r) // 2
        if mid ** 2 <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


# **思想： 牛顿法
# - 通过推导迭代公式为：  x = 1/2 * （x + a / x)    // a是目标值

def my_sqrt(x):
    if x < 0:
        raise Exception('不能输入负数')
    if x == 0:
        return 0
    cur = 1
    while True:
        pre = cur
        cur = (cur + x / cur) / 2
        if abs(cur - pre) < 1e-6:
            return int(cur)
