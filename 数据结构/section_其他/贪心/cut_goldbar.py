"""
问题：一块金条切成两半，是需要花费和长度数值一样的铜板的。比如
长度为20的 金条，不管切成长度多大的两半，都要花费20个铜
板。一群人想整分整块金 条，怎么分最省铜板？
例如,给定数组{10,20,30}，代表一共三个人，整块金条长度为
10+20+30=60. 金条要分成10,20,30三个部分。 如果， 先把长
度60的金条分成10和50，花费60 再把长度50的金条分成20和30，
花费50 一共花费110铜板。
但是如果， 先把长度60的金条分成30和30，花费60 再把长度30
金条分成10和20，花费30 一共花费90铜板。
输入一个数组，返回分割的最小代价。
"""

# 思路：
# 切的过程反过来就是组合的过程，找切的最小代价就可以看作组合的最小代价
# 采用类似于霍夫曼编码的思想
# 建立小根堆
# 每次选两个最小的进行组合，将组合好的新值就是组合的代价，组合的新值重新放入堆中
# 直到只有一块金条
# 注： 贪心就是每次拿出指标值最好的元素，这与堆的结构符合

import heapq
import numpy as np


def less_money(arr):
    heapq.heapify(arr)
    total = 0
    while len(arr) > 1:
        num1 = heapq.heappop(arr)
        num2 = heapq.heappop(arr)
        new_num = num1 + num2
        total += new_num
        heapq.heappush(arr, new_num)
    return total


if __name__ == "__main__":
    lis = list(np.random.randint(1, 10, (3,)))
    print(lis)
    print(less_money(lis))
