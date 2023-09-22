
""" n, m, k_n, k_m = list(map(int, input().split()))

def max_onestep(row, col, k_n, k_m, last_max):
    if col == 1:
        res = 0
        for i in range(row + k_n):
            for j in range(col + k_m):
                if i*j % 10 > res:
                    res = i*j % 10
        return res
    else:
        for j in range(col + k_m):
            i = row + k_n - 1
            if i * j % 10 > last_max:
                last_max = i * j % 10
        return last_max
                
# 遍历每个左上角点的坐标
res = 0

for i in range(1, (n-k_n+2)):
    last_max = 0
    for j in range(1, (m-k_m + 2)):
        last_max = max_onestep(i, j, k_n, k_m, last_max)
        res += last_max
print(res)
 """



n, m, k_n, k_m = list(map(int, input().split()))


def max_onestep(row, col, k_n, k_m):
    res = 0
    for i in range(row + k_n):
        for j in range(col + k_m):
            if i*j % 10 > res:
                res = i*j % 10
    return res


# 遍历每个左上角点的坐标
res = 0
for i in range(1, (n-k_n+2)):
    for j in range(1, (m-k_m + 2)):
        res += max_onestep(i, j, k_n, k_m)
print(res)
 