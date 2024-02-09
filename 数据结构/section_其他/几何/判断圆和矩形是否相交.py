import math


def process(radius, x_center, y_center, x1, y1, x2, y2):
    # 1. 以radius+长为半径画圆
    h, w = (x2 - x1), (y2 - y1)
    rec_center = ((x1 + x2) / 2, (y1 + y2) / 2)
    half_long_side = max(h, w) / 2
    dis = math.sqrt(pow(rec_center[0] - x_center, 2) + pow(rec_center[1] - y_center, 2))
    if dis <= radius + half_long_side:
        return True

    # 2 以radius+对角线为半径画圆
    half_diag = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    if dis > radius + half_diag:
        return False

    # 3 判断离圆最近的角是否在圆内
    dis1 = math.sqrt(pow(x1 - x_center, 2) + pow(y1 - y_center, 2))
    dis2 = math.sqrt(pow(x2 - x_center, 2) + pow(y2 - y_center, 2))
    dis3 = math.sqrt(pow(x1 - x_center, 2) + pow(y2 - y_center, 2))
    dis4 = math.sqrt(pow(x2 - x_center, 2) + pow(y1 - y_center, 2))
    dises = [dis1, dis2, dis3, dis4]
    for dis in dises:
        if dis <= radius:
            return True
    return False


import sys
lines = sys.stdin.readlines()
for line in lines:
    line.strip()
    arr = [int(item) for item in line.split(' ')]
    print(process(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6]))



