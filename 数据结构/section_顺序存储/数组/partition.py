# 题目（Partition）：给定一个数组arr，和一个数num，请把小于等于num的数放在数
# 组的左边，大于num的数放在数组的右边。


# 思想：
# - 将数组看作有两个部分，左半部分是小于等于num的部分，右半部分是大于num的部分
# 刚开始左半部分在数组的-1位置，small是左半部分的下一个，
# 而整个数组看作右半部分
# - 遍历右半部分，如果遍历到应该属于左半部分的值，将其与small交换，左半部分容量加一
def partition(arr, num=3):
    small = 0
    for i in range(len(arr)):
        if arr[i] < num:
            arr[i], arr[small] = arr[small], arr[i]
            small += 1
    return arr


# 题目（荷兰国旗问题，其实就是能分三个部分的partition）：给定一个数组arr，和一个数num，
# 请把小于num的数放在数组的左边，等于num的数放在数组的中间，大于num的数放在数组的右边。
# 思想：在最后增加一个指针，该方法可以应对任何想把数组分为三份的要求。
# 思想：将数组看作有三个部分，左半部分是小于等于num的部分，中间部分是等于num的部分，右半部分是大于num的部分
# 刚开始左半部分在数组的-1位置，而整个数组看作中间部分，数组的右边是右半部分
# small是左半部分的下一个，large是右半部分的上一个
# 遍历右半部分，如果遍历到应该属于左半部分的值，将其与small交换，换过来什么值并不重要，重要的是换过去的一定是属于左半部分的


def netherland_flag_problem(arr, num=0):
    small = 0
    large = len(arr) - 1  # 注意这里的large是大于num区域的前一个数的索引
    cur = 0
    while cur <= large:  # cur指针只需要重新判断中间部分的值，到了右边的边界，则停止
        if arr[cur] < num:  # 属于左半部分的
            arr[cur], arr[small] = arr[small], arr[cur]
            small += 1
            cur += 1  # 由于cur比small先
            # 判断，small所在值交换过来不用重新判断，可以继续往前走
            # 直接去掉这句也行
        elif arr[cur] > num:
            arr[cur], arr[large] = arr[large], arr[cur]
            large -= 1  # 交换了，但是交换来的数不一定满足要求
        else:
            cur += 1
    return arr
