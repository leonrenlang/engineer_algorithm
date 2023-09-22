# 1. 建堆的时间复杂度是O(n)
#         - log1 + log2 + .... logn
# 2. 建堆之后就能连续以log(n)的代价获取最大/最小值
# 时间复杂度：
# - 增 O(logn)
# - 删：最大/最小值 O(logn)   |  其他O(n),因为需要先找到目标值，然后做调整
# - 查：最大/最小值 O(1)       | 其他O(n)
# - 改：找到相应的值O(n)， 值的修改可能使得不满足堆的定义，需进行相应的修改

# 实现细节
# - 任意一个节点的值大于或小于其父节点的值，注：不一定大于其父的兄弟
# - 堆是一棵抽象的完全二叉树
#   一个节点的左右孩子分别是2*i + 1， 2*i + 2
#   一个节点的父节点的是 (i-1) // 2
# - 优先队列就是堆，堆是实质的物理结构，优先队列是应用的名字， 可以把堆节点的值看作其优先级，优先级高的先出队


def heap_insert(arr, index):
    # 对index所指的元素，自底向上调整，大根堆
    while index > 0 and arr[index] > arr[(index - 1) // 2]:
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2


def heapify(arr, index, size):
    # 对index所指元素向下调整，size是堆的元素个数
    left = index * 2 + 1
    while left < size:  # 如果结点有孩子，才继续循环
        if left + 1 < size:  # 如果右孩子存在
            large = left if arr[left] > arr[left + 1] else left + 1
        else:
            large = left
        if arr[index] > arr[large]:
            break
        else:
            arr[index], arr[large] = arr[large], arr[index]
        index = large
        left = index * 2 + 1


def convert_to_heap():
    pass


def heap_sort(arr):
    if len(arr) < 2: return arr
    for i in range(1, len(arr)):  # 建大根堆
        heap_insert(arr, i)
    size = len(arr) - 1  # 依次把大的数往后面放
    swap(arr, 0, size)  # 把最大的数放到最后面
    while size > 0:
        heapify(arr, 0, size)  # # 对根节点进行自上而下的调整 size是边界的右边一个
        size -= 1
        swap(arr, 0, size)
    return arr


def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


def get_k_largest(arr, k):
    arr_copy = arr[:]
    for i in range(len(arr_copy)):
        heap_insert(arr_copy, i)  # 建大根堆
    res = []
    for i in range(k):
        res.append(arr_copy[0])  # 获取数据
        swap(arr_copy, 0, -(i + 1))
        heapify(arr_copy, 0, size=len(arr_copy) - (i + 1))
    return res


if __name__ == "__main__":
    lis = [-4, 3, -3, 9, 12, 2, 3, 4, 5, 54, 234, 5, 45, 3, 5, 5, 5, 34, 23, 2, 34]
    heap_sort(lis)
    print(get_k_largest(lis, 2))
    print(lis)
