# 逆序对问题，在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对，请打印所有逆序对。
# 输入: [7,5,6,4]
# 输出: 5

def correct_reverse_pairs(lis: list):
    '''
        双重循环，遍历所有可能的两两组合，判断是否为逆序对
    '''
    if len(lis) < 2: return 0
    res = 0
    for i in range(len(lis) - 1):
        for j in range(i + 1, len(lis)):
            if lis[i] > lis[j]:
                res += (lis[i], lis[j])
    return res


''' 为什么在归并排序的过程中可以取得所有的逆序对？
1. 首先，一上来我们把数据分成了两半，左边的一半归并前和右边的一半完全不会产生逆序对
2. 那么如果在归并过程中，我们能把两个数组之间的所有逆序对输入，则归并排序过程能达到最初的目标
3. 在归并排序的过程中，
'''
def reverse_pairs2(lis):
    # 采用从大到小的方式求逆序对，更高效
    def merge(lis, L, mid, R):
        # 两个有序数组合并的构成中，输出可能的逆序对
        p1 = L
        p2 = mid + 1
        tmp = []
        res = 0
        while p1 <= mid and p2 <= R:
            if lis[p1] > lis[p2]:
                tmp.append(lis[p1])
                p1 += 1
                res += (R - p2 + 1)
            else:
                tmp.append(lis[p2])
                p2 += 1
        tmp += lis[p1:mid + 1]
        tmp += lis[p2:R + 1]
        lis[L:R + 1] = tmp
        return res

    def process(lis, L, R):
        if L >= R: return 0
        mid = (L + R) // 2
        left = process(lis, L, mid)
        right = process(lis, mid + 1, R)
        cur = merge(lis, L, mid, R)
        return left + right + cur

    return process(lis, 0, len(lis) - 1)


def reverse_pairs(lis: list):
    # 虽然是求逆序对，但是归并排序的方向仍然是从小到大
    if len(lis) < 2: return 0

    def merge(lis, L, mid, R):
        p1 = mid
        p2 = R
        tmp = [0] * (R - L + 1)
        tmp_index = R - L
        res = 0
        while p1 >= L and p2 >= mid + 1:
            if lis[p1] > lis[p2]:
                tmp[tmp_index] = lis[p1]
                p1 -= 1
                tmp_index -= 1
                res += (p2 - mid)
            else:
                tmp[tmp_index] = lis[p2]
                p2 -= 1
                tmp_index -= 1
        while p1 >= L:
            tmp[tmp_index] = lis[p1]
            p1 -= 1
            tmp_index -= 1
        while p2 >= mid + 1:
            tmp[tmp_index] = lis[p2]
            tmp_index -= 1
            p2 -= 1
        lis[L:R + 1] = tmp
        return res

    def process(lis, L, R):
        if L == R: return 0
        mid = (L + R) // 2
        return process(lis, L, mid) + process(lis, mid + 1, R) + merge(lis, L, mid, R)

    return process(lis, 0, len(lis) - 1)
