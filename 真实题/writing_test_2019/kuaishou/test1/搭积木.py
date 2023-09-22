# 问题：有一堆长宽不一的积木，要将这些积木堆叠起来，要求上面的积木的长宽小于等于下面的积木
# 求最多能搭几层

# 输出描述:
# 输出总共可以搭的层数
# 示例1
# 输入
# 复制
# 5
# 2 2
# 2 4
# 3 3
# 2 5
# 4 5
# 输出
# 复制
# 4
from bisect import bisect


# 思想：把长或者宽其中一个排好序，然后对另一个求最长子序列问题
# 建立一个辅助数组，期望数组内是一个最长子序列，遍历源数组，将每个元素放到
# 其刚好大于的位置。用二分找到该位置
# 注意：这里的最长子序列允许序列中有重复值，故其逻辑与bisect(bisect_right)一致
def process2(bricks):
    bricks = sorted(bricks, key=lambda item: item[0])
    lis = len(bricks) * [0]
    res = 0
    for brick in bricks:
        index = bisect(lis, brick[1], lo=0, hi=res)  # 找到应该插入的位置
        lis[index] = brick[1]
        if index == res:  # 如果插在尾部，则整体长度加1
            res += 1
    print(res)
    return res


def process1(bricks):
    bricks = sorted(bricks, key=lambda item: item[0])
    lis = []
    for brick in bricks:
        if not lis:
            lis.append(brick[1])
        elif lis[-1] <= brick[1]:
            lis.append(brick[1])
        else:
            index = bisect(lis, brick[1])
            lis[index] = brick[1]
    print(len(lis))


def main():
    n = int(input())
    bricks = []
    for _ in range(n):
        L, W = [int(item) for item in input().split()]
        bricks.append((L, W))
    process1(bricks)
    process2(bricks)


if __name__ == '__main__':
    main()
