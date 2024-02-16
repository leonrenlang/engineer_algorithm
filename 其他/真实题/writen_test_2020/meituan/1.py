import random
import sys 
import math


day = int(input())
h, m = list(map(int,input().split(':')))
back_min = int(input())

cur_min = h * 60 + m
res_min = cur_min - back_min
if res_min >= 0:
    print(day)
    print(str(res_min//60)+':'+str(res_min%60))
else:
    minus_day = abs(res_min // (24*60))
    day = (day-minus_day+7) % 7
    res_min = (res_min+(24*60)) % (24*60)
    print(day)
    print(str(res_min//60)+':'+str(res_min%60))
