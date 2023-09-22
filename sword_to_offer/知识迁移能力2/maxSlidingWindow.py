

# 题目1：给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
# 思路：维护一个双端队列（两边都可以pop），对于每个数做如下操作
# 队列中数太多了吗， 将队列中小于当前元素的都pop, 将当前元素加入进来
# 队列的第一个就保持为最大值

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, result = deque(), list()

        for i in range(len(nums)):
            if queue and queue[0] == i - k:
                # 如果最大值在当前滑动窗口之外，去掉它
                queue.popleft()
            
            while queue and nums[queue[-1]] < nums[i]:
                # 将小于当前元素的，全部从队列中推出
                queue.pop()

            queue.append(i)  # 将当前元素加入队列
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result

""" 题目2：请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1
 """

class MaxQueue(object):
    def __init__(self):
        self.queue = []
        self.max_queue = []
        
    def max_value(self):
        """
        :rtype: int
        """
        if not self.max_queue:
            return -1
        else:
            return self.max_queue[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)
    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queue:
            return -1
        elif self.max_queue[0] == self.queue[0]:
            self.max_queue.pop(0)
            return self.queue.pop(0)
        else:
            return self.queue.pop(0)