
'''
    
'''

def count_sort(lis):
    # 计数排序
    if len(lis) < 2: return lis
    min, max = lis[0], lis[0]
    for item in lis:
        if item < min:
            min = item
        elif item > max:
            max = item
    bucket = [0] * (max - min + 1)
    for item in lis:
        bucket[item - min] += 1
    res = []
    for i in range(len(bucket)):
        while bucket[i] != 0:
            res.append(min + i)
            bucket[i] -= 1
    return res
