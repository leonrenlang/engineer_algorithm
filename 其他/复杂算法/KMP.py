# 问题： 判断字符串2是否是字符串1是子串，是的话返回索引。


# 分析：
# 如果暴力，时间O(M*N)，假设较长的字符串长度为N, 较短的长度为M


# 思想：
# - 首先建立一个新概念： 字符串中某个字符前面的 最长前缀 和 最长后缀 的匹配长度
# - 比如说abcabcd，前缀长度和后缀长度都取1，不匹配；取2，不匹配；取3，匹配；
# 取4，不匹配； 取5，不匹配；因此d位置的最长前缀和最长后缀的匹配长度为3。
# - abcabcd中的每个字符的最长前缀和后缀匹配长度组成的数组 [-1, 0, 0, 0, 1, 2, 3]，默认0位置为-1
# 这个数组通常叫做 “next” 数组
# - str2与str1的某个位置的字符开始比较，假设到了某一个字符不匹配了，
# 根据next数组，我们已经知道这个字符的最长前缀和最长后缀的匹配长度
# 那么我们就可以从str1中失败位置减去 匹配长度 开始与str2的0位置开始匹配
# 并且我们已知前面有 匹配长度 个字符是可以匹配上的, 直接跳过匹配长度即可。
def get_index_of(str1, str2):
    if not str1 or not str2 or len(str1) < len(str2):
        return -1
    p1 = 0
    p2 = 0
    next_arr = get_next_arr(str2)  # 得到str2的next数组
    while p1 < len(str1) and p2 < len(str2):
        if str1[p1] == str2[p2]:
            p1 += 1
            p2 += 1
        elif next_arr[p2] == -1:  # 不等情况1:索引p2对应的匹配数是-1，说明p2指向的是0，第一个字符没配上
            p1 += 1
        else:  # 不等情况2:
            p2 = next_arr[p2]  # p2指向前缀后一个数
    return (p1 - p2) if p2 == len(str2) else -1


# 快速计算next数组方法：
# - 对于每个字符，已知其前一个元素的匹配长度，如果已知前缀的匹配长度后一个字符
# 等于当前的前一个字符，则当前的字符的匹配长度为前一个字符的匹配长度+1
# 例子： abcabcab 求最后一个b的匹配长度，b前面你的a的匹配长度为3，则b的匹配长度为4
# - 如果不等，则找到前缀（"abc") 的后一个字符a，找它的最长前缀的后一个字符与当前字符的前一个字符
# 是否匹配，如果匹配，则当前字符的匹配长度为上述a的匹配长度+1，否则，重复上述过程，
# 直到没有办法找到匹配
# 例子： ababcababtk   t的匹配为4，但是abab的后一个字符c不等于t；找到t,t的匹配为2, ab的后一个字符a也不等
# 于t，又没匹配上；所以在k这个位置的匹配就是0.
def get_next_arr(str2):
    # 生成next数组
    if len(str2) == 1:
        return [-1]
    next_arr = [0] * len(str2)
    next_arr[0] = -1
    idx = 2  # 前两个已知
    cn = 0  # cn是前缀的后一个位置
    while idx < len(next_arr):
        if str2[idx - 1] == str2[cn]:  # 如果前缀的后一个位置和我前一个字符是一样的
            cn += 1  # 更新前缀的后一个位置
            next_arr[idx] = cn  # 前缀的后一个位置的索引，也就是当前的匹配数
            idx += 1
        elif cn > 0:  # 如果前缀的后一个位置和我前一个字符不相等，
            # 可以继续往前跳，那就往前跳
            cn = next_arr[cn]
        else:  # 如果不能往前跳了，当前位置的匹配数就是0了。
            next_arr[idx] = 0
            idx += 1
    return next_arr


if __name__ == "__main__":
    str1 = 'I am chinese'
    str2 = 'am '
    print(get_index_of(str1, str2))
