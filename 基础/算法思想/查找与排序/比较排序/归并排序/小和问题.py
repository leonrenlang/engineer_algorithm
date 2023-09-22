# 小和问题:在一个数组中，每一个数的左边 比当前数小的数累加起来，叫做这个数组的小和。
# 求一个数组的小和。
""" 例子：
[1,3,4,2,5]
1左边比1小的数，没有；
3左边比3小的数，1；
4左边比4小的数，1、3；
2左边比2小的数，1；
5左边比5小的数，1、3、4、2；
所以小和为1+ 1+3 + 1 + 1+3+4+2 =16 """

'''
    为什么小和问题可以用归并排序的过程？
    1. 假设左右两边都进行了排序过程，目前左右两边已经按照从小到大排序了
    2. 遍历过程中，每次找到左边比当前数小的数，然后累加，即完成右边每一个数对左边的小和计算
    3. 而左右两个有序数组内部的小和计算交给递归过程
'''

def correct_small_sum(lis):
    if len(lis) < 2: return 0
    res = 0
    for i in range(1, len(lis)):
        for j in range(0, i):
            if lis[j] < lis[i]:
                res += lis[j]
    return res


def small_sum(lis: list):
    def merge(lis, L, mid, R):
        tmp = []
        p1, p2 = L, mid + 1
        res = 0
        while p1 <= mid and p2 <= R:
            if lis[p1] < lis[p2]:
                tmp.append(lis[p1])
                res += (R - p2 + 1) * lis[p1]
                p1 += 1
            else:
                tmp.append(lis[p2])
                p2 += 1
        tmp += lis[p1:mid + 1]
        tmp += lis[p2:R + 1]
        lis[L:R + 1] = tmp
        return res

    def process(lis, L, R):
        if L == R: return 0
        mid = (L + R) // 2
        left = process(lis, L, mid)
        right = process(lis, mid + 1, R)
        cur = merge(lis, L, mid, R)  # 在这里，左右两个子问题的最小和已经求解完毕，并且左右两个子数组都是有序的
        return left + right + cur

    return process(lis, 0, len(lis) - 1)
