import heapq

# 说明：
# - heapq是小根堆


# 常用操作
# 1. 建堆，将不是堆的数组转换成一个堆
# lis = [10, 3, 4, 6, 2, 7]
# heapq.heapify(lis)
# print(lis)

# 2. heappush(heap, item)， heappop(item)
# - heappush: 在最末尾增加目标元素，从下往上调整
# - heappop：将最小的值弹出，然后将最后一个值赋给第一个数，从上往下调整
    
# 3. heapreplace, heappushpop
# heapreplace 相当于先pop,再push
# heappushpop 先push再pop
# a = [2, 3, 4, 5, 6]
# heapq.heapify(a)
# b = a[:]
# heapq.heappushpop(a, -1)
# print(a)   # [2, 3, 4, 5, 6]
# heapq.heapreplace(b, -1)
# print(b)   # [-1, 3, 4, 5, 6]


# 4. nsmallest(n, iterable, key=None), nlargest(n, iterable, key=None)
# a = [2, 3, 4, 5, 6, 5]
# print(heapq.nsmallest(3, a))  # [2 , 3, 4]
# print(a)  # [2, 3, 4, 5, 6, 5]
# print(heapq.nlargest(2, a))  # [6, 5]
# print(a)  # [2, 3, 4, 5, 6, 5]


arr = [(1, 3), (5, 2),(3, 4)]
heapq.heapify(arr)
