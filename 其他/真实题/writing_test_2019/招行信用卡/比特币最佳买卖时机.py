# 问题：给定一个数组，里面是每天比特币的价格，允许进行一次交易，求最大利润


def process(arr):
    import sys
    dp_i_0 = 0
    dp_i_1 = -sys.maxsize
    for i in range(len(arr)):
        dp_i_0 = max(dp_i_0, dp_i_1 + arr[i])
        dp_i_1 = max(dp_i_1, -arr[i])
    print(dp_i_0)


if __name__ == '__main__':
    arr = [int(item) for item in input().split()]
    process(arr)
