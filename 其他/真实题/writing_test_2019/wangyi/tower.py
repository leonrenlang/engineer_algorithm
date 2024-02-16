# 问题：小易有一些立方体，每个立方体的边长为1，他用这些立方体搭了一些塔。
# 现在小易定义：这些塔的不稳定值为它们之中最高的塔与最低的塔的高度差。
# 小易想让这些塔尽量稳定，所以他进行了如下操作：每次从某座塔上取下一块立方体，并把它放到另一座塔上。
# 注意，小易不会把立方体放到它原本的那座塔上，因为他认为这样毫无意义。
# 现在小易想要知道，他进行了不超过k次操作之后，不稳定值最小是多少。


def main():
    n, k = [int(item) for item in input().split(' ')]
    tower_heights = [int(item) for item in input().split(' ')]

    strs_savetoprint = []
    stale_num = -1
    operation_times = -1
    for times in range(k):
        min_idx = 0
        max_idx = 0
        for idx in range(len(tower_heights)):
            if tower_heights[idx] > tower_heights[max_idx]:
                max_idx = idx
            if tower_heights[idx] < tower_heights[min_idx]:
                min_idx = idx
        if tower_heights[max_idx] == tower_heights[min_idx]:
            operation_times = k + 1
            break
        tower_heights[max_idx] -= 1
        tower_heights[min_idx] += 1
        stale_num = tower_heights[max_idx] - tower_heights[min_idx]
        strs_savetoprint.append(str(max_idx + 1) + ' ' + str(min_idx + 1))
        operation_times = times + 1
    print(str(stale_num) + ' ' + str(operation_times))
    for item in strs_savetoprint:
        print(item)


if __name__ == '__main__':
    main()
