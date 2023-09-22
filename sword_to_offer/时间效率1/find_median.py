import heapq

#  数据流中的中位数
# 思路：
# 假想我们现在有两个容器 A, B 这两个容器将我们的整体数据分成两部分,且 A 中的数据都小于 B 中的数据,并且 A 中的最后一个数据是 A 里面最大的
# B 的第一个数据是 B 中最小的.
# 好了 我们有了上面的条件,那我们怎么找到中位数呢?
# 当整体数目为奇数时,中间的那个数就是所求.当整体数目为偶数时,中间两个数的和再除以 2 ,就能得到结果
# 但这和我们上面的两个容器有什么关系呢?
# 我们只要将上面的两个容器的数据数目只差保持在 1 之内即可,也就是说 A 和 B 将整体数据以中位数划分开来了


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [] # 前半部分
        self.min_heap = [] # 后半部分
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num)) # num放大根堆
        else:
            # 当数据流为奇数个时候，说明最小堆个数和最大堆个数不一样，这里我放在后半部分（最小堆）
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num)) # num放小根堆
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] + -1 * self.max_heap[0]) / 2
        else:
            return self.min_heap[0]
