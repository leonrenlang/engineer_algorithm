# 归并排序, 原地排序,归并可以帮助理解递归复杂度算法(主方法)
# 为什么归并比一般O(n2)快，因为右边全部排好序之后，左边就只要和右边的一个值进行比较，会有更少浪费掉的比较，所以就快。


def merge_sort(lis):
    ''' 归并排序
        
    思想，将数组均分为两部分，分别排序后，将两个有序数组合并O(N)
    如果数组的长度为2，划分后再合并相当于进行比较
    如果数组长度小于等于1，停止递归
    '''
    def merge(lis, L, mid, R):
        '''
            merge操作的作用是：将两个有序数组合并成一个有序数组
            左边的队列 [L, mid], 右边的队列 [mid + 1, R]
        '''
        tmp = []
        p1, p2 = L, mid + 1
        while p1 <= mid and p2 <= R:
            if lis[p1] < lis[p2]:
                tmp.append(lis[p1])
                p1 += 1
            else:
                tmp.append(lis[p2])
                p2 += 1
        tmp += lis[p1:mid + 1]
        tmp += lis[p2:R + 1]
        lis[L:R + 1] = tmp  # 就是一个单纯的赋值行为，不涉及到对象引用的变换

    def process(lis, L, R):
        '''
            process 操作的作用是对数组指定范围进行排序
        '''
        # 给定一个数组与一个范围，将范围内数据排序
        if L >= R: return None
        mid = (L + R) // 2  # 将数组划分为两个部分[L, mid] [mid, R]
        process(lis, L, mid)
        process(lis, mid + 1, R)
        merge(lis, L, mid, R)

    process(lis, 0, len(lis) - 1)
    return lis


if __name__ == "__main__":
    lis = [5, 325, 123, 1231, 34234, 234, 234, 234, 2, 523, 545, 53]
    print(lis)
    print(merge_sort(lis))
