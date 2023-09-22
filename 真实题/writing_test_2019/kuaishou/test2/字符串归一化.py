# 题目描述
# 通过键盘输入一串小写字母(a~z)组成的字符串。
# 请编写一个字符串归一化程序，统计字符串中相同字符出现的次数，并按字典序输出字符及其出现次数。
# 例如字符串"babcc"归一化后为"a1b2c2"

# 输入描述:
# 每个测试用例每行为一个字符串，以'\n'结尾，例如cccddecca
# 输出描述:
# 输出压缩后的字符串ac5d2e

# 示例1
# 输入
# dabcab
# 输出
# a2b2c1d1

# 思想：
# -创建一个26个元素的数组，分别代表a~z，遍历string。
# -其实就是计数排序
def process(string):
    arr = [0] * 26
    for ch in string:
        arr[ord(ch) - 97] += 1
    res = ''
    for idx in range(len(arr)):
        if arr[idx] != 0:
            res += (chr(idx + 97) + str(arr[idx]))
    print(res)


# 代码简单，时间复杂度高(有排序）
def process(string):
    lis = sorted(list(set(string)))
    for item in lis:
        num = string.count(item)
        print(item + str(num), end='')


if __name__ == '__main__':
    string = input()
    # print(ord('a'))
    process(string)
