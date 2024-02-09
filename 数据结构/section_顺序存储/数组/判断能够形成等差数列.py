# 如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。
# 示例 1：
# 输入：arr = [3,5,1]
# 输出：true
# 解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
# 示例 2：
# 输入：arr = [1,2,4]
# 输出：false
# 解释：无法通过重新排序得到等差数列。


# 思想：
# - 第一次遍历，找到maxi, mini, 把所有的值入hash表
# - 第二次遍历，判断从[mini:maxi:gap]的数是否在hash表中
def process(arr):
    maxi = arr[0]
    mini = arr[0]
    dic = {}
    for item in arr:
        if item > maxi:
            maxi = item
        if item < mini:
            mini = item
        dic[item] = ''
    gap = (maxi - mini) // (len(arr) - 1)
    if not isinstance(gap, int):
        return False
    cur = mini + gap
    while cur < maxi:
        if cur not in dic.keys():
            return False
        cur += gap
    return True


if __name__ == '__main__':
    lis = [1, 3, 5, 6]
    print(process(lis))