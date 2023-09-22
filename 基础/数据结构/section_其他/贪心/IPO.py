import bisect
import heapq

"""  
问题：给定两个数组，其中一个数组代表每个项目的花费，另一个代表每个项目的利润。
只能同时做一个项目，给定初始资金init_money和能投资的次数k，求最大利润
"""


# 思想：最朴素的想法，遍历数组，将所有能做的项目取出，然后遍历取出的数组，找到利润最高的项目。
def max_profit2(costs, profits, init_money, k):
    for _ in range(k):
        affordable = []
        for idx, cost in enumerate(costs):
            if init_money >= cost:
                affordable.append(idx)
        profit = 0
        for idx in affordable:
            if profit < profits[idx]:
                profit = profits[idx]
        init_money += profit
    return init_money


# 思想：
#   1.由于需要进行k轮投资，每次都遍历时间损耗有点高，因此将按花费将数组做成一个堆（其实也可以直接排序）
#   每次将能做的项目取出

#   2.取出后的项目放入大根堆中，按照项目的利润进行排序，堆顶既是目标项目。
#   由于init_money一定的单调递增的，因此之前从小根堆转移到大根堆的项目可以复用，只需再拿一部分新的可以
#   进行的项目转移到大根堆即可。
#   3.实现时，该思路的问题是，python中的堆不支持自定义比较器，自定义了一个可以用key的堆
def max_profit(costs, profits, init_money, k):
    programs = [Program(cost, profit) for cost, profit in zip(costs, profits)]
    cost_heap = MyHeap(programs, key=lambda program: program.cost)
    profit_heap = MyHeap(key=lambda program: program.profit * (-1))

    for _ in range(k):

        tmp = cost_heap.data[0][0]
        while init_money >= tmp:
            profit_heap.push(cost_heap.pop())
            tmp = cost_heap.data[0][0]
        init_money += (profit_heap.data[0][1].profit)
    return init_money


# ***支持自定义key lambda函数的堆
class MyHeap(object):
    def __init__(self, initial=None, key=lambda x: x):
        self.key = key
        if initial:
            self.data = [(key(item), item) for item in initial]
            heapq.heapify(self.data)
        else:
            self.data = []

    def push(self, item):
        heapq.heappush(self.data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self.data)[1]


class Program:
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit


if __name__ == '__main__':
    costs = [12, 2312, 3, 23, 4234, 2314, 800, 5]
    profits = [123, 12, 3, 324, 23, 42, 34, 23]
    init_money = 50
    k = 5
    res = max_profit2(costs, profits, init_money, k)
    print(res)
