import heapq

# 问题：设计一个数据结构

class MedianFinder:
    # 为什么要写成一个类？为了应对流式数据，如果直接是一个数组，没有必要写成一个类
    def __init__(self):

        self.bigroot_heap = []  # 前半部分,大根堆
        self.littleroot_heap = []  # 后半部分,小根堆

    def add_num(self, num: int) -> None:

        if len(self.bigroot_heap) == len(self.littleroot_heap):  # 规定如果两个堆数据量相同，放后面
            heapq.heappush(self.littleroot_heap, -heapq.heappushpop(self.bigroot_heap, -num))  # num放大根堆
        else:  # 数据量不同，放大根堆，前半部分
            heapq.heappush(self.bigroot_heap, -heapq.heappushpop(self.littleroot_heap, num))  # num放小根堆

    def get_median(self) -> float:
        if len(self.bigroot_heap) == len(self.littleroot_heap):
            return (self.littleroot_heap[0] + -1 * self.bigroot_heap[0]) / 2
        else:
            return self.littleroot_heap[0]


if __name__ == '__main__':
    lis = [-4, 3, -3, 9, 12, 2, 3, 4, 5, 54, 234, 5, 45, 3, 5, 5, 5, 34, 23, 2, 34]
    medianfinder = MedianFinder()
    for item in lis:
        medianfinder.add_num(item)
        print(medianfinder.get_median())
