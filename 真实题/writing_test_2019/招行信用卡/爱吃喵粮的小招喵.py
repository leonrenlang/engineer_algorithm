# 题目描述
# 小招喵喜欢吃喵粮。这里有 N 堆喵粮，第 i 堆中有 p[i] 粒喵粮。喵主人离开了，将在 H 小时后回来。
# 小招喵可以决定她吃喵粮的速度 K （单位：粒/小时）。每个小时，她将会选择一堆喵粮，从中吃掉 K 粒。如果这堆喵粮少于 K 粒，她将吃掉这堆的所有喵粮，然后这一小时内不会再吃更多的喵粮。
# 小招喵喜欢慢慢吃，但仍然想在喵主人回来前吃掉所有的喵粮。
# 返回她可以在 H 小时内吃掉所有喵粮的最小速度 K（K 为整数）。

# 输入描述:
# 第一行输入为喵粮数组，以空格分隔的N个整数
# 第二行输入为H小时数
# 输出描述:
# 最小速度K

# 示例1
# 输入
# 3 6 7 11
# 8
# 输出
# 4

def judge_speed(arr, hour, speed):
    # 如果当前速度可行，返回True
    need_hour = 0
    for item in arr:
        need_hour += (item - 1) // speed + 1
    return need_hour <= hour


def bisearch(arr, L, R, hour):
    while L <= R:
        mid = (L + R) // 2
        if judge_speed(arr, hour, mid):
            R = mid - 1
        else:
            L = mid + 1
    print(L)


if __name__ == '__main__':
    arr = [int(item) for item in input().split()]
    hour = int(input())
    if hour < len(arr):
        print('Impossible')
    max_num = max(arr)
    bisearch(arr, 1, max_num, hour)
