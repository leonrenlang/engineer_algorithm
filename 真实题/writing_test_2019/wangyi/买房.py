
# 问题：有n幢房子，k个住户，住户所在的位置不定，我希望搬进去，但我希望我左右都有邻居
# 求最少符合要求的房子数，和最多符合要求的房子数

# 思想：
#
def process(n, k):
    if k == 0:
        return 0, 0
    if k > (n + 1) // 2:
        k = (n + 1) - k
    return 0, k - 1


# TODO
def process(n, k):
    if 2 * k -1 <= n:
        return 0, k-1
    else:
        return 0,

def main():
    num_instance = int(input())
    for _ in range(num_instance):
        n, m = [int(item) for item in input().strip().split()]
        res = process(n, m)
        print(str(res[0]) + ' ' + str(res[1]))


if __name__ == '__main__':
    main()
