""" 说明1：冒泡和选择工程上已经没有人用了，在数据量小的时候，插入排序还比较有用
    说明2：
        一般排序默认为从小到大排序
        实现的版本都是原地排序
 """
import copy



def insert_sort(lis: list) -> list:
    ''' 插入排序 

    1. 一共进行n-1轮
    2. 假设第一个元素已经是有序的序列，将其视为已排序序列。从第二个元素开始，依次将每个元素插入到已排序序列中的适当位置。
    对于当前要插入的元素，从已排序序列的末尾开始向前比较，将比它大的元素向后移动，直到找到合适的位置插入。
    '''
    # 插入排序
    if not lis or len(lis) < 2:   return lis



    for i in range(1, len(lis)):  # i指向每次要向前放的牌
        for j in reversed(range(0, i)):  # 依次遍历i-1 ... 0
            if lis[j + 1] < lis[j]:
                lis[j + 1], lis[j] = lis[j], lis[j + 1]
    return lis


def bubble_sort(lis: list) -> list:
    '''冒泡排序
    
    1. 一共进行n-1轮
    2. 每轮将范围内的元素中最大的传递到最后面
    '''
    if not lis or len(lis) < 2:   return lis
    for i in range(1, len(lis)):  # 相当于规定了一次冒泡的范围[0,len(lis)-i)
        for j in range(len(lis) - i):
            if lis[j] > lis[j + 1]:  # 改成“<”则为从大到小
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis

def select_sort(input_lis):
    ''' 选择排序
    1. 一共进行n-1轮
    2. 每轮遍历找到范围内最小的元素
    3. 将最小的元素放到最前面
    '''
    lis = copy.deepcopy(input_lis)
    if not lis or len(lis) < 2: return lis

    for i in range(0, len(lis)-1):
        min_idx = i
        for j in range(i+1, len(lis)):
            if lis[j] < lis[min_idx]:
                min_idx = j
        lis[i], lis[min_idx] = lis[min_idx], lis[i]
    return lis
            

def correctSort(array):
    return sorted(array)


if __name__ == "__main__":
    import numpy as np
    lis = list(np.random.randint(1, 10000, (10,)))
    print(lis)
    my_resort = select_sort(lis)
    print(my_resort)
    correct = correctSort(lis)
    print(my_resort == correct)
    
