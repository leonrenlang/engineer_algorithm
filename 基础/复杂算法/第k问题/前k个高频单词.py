import collections
import heapq


# 问题：给一个单词列表，返回前k个频率最高的单词


# 思想： 堆
def top_k_frequent(words, k):
    dic = collections.Counter(words)
    heap, ans = [], []
    for key in dic:
        heapq.heappush(heap, (-dic[key], key))
    for _ in range(k):
        ans.append(heapq.heappop(heap)[1])
    return ans


class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# 思想： 排序
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key=lambda w: (-count[w], w))
        return candidates[:k]
