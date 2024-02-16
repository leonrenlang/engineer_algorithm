# 题目描述
# 输入两个字符串a和b，字符串内容为二进制数字，求两个字符串相加的结果，加法计算方法以二进制方式计算，
# 并返回对应的字符串结果。要求程序尽可能的高效。示例如下：

# 输入描述:
# 输入两个字符串，如"1101", "1100"
# 输出描述:
# "11001"

# 示例1
# 输入
# 1101 1100
# 输出
# 11001

# 思想：
# - 将每个输入的长度填充到max(inputs) + 1
# - 用一个res列表保存结果，按位进行计算即可
def add(str1, str2):
    len_paded = max(len(str1), len(str2)) + 1
    str1 = '0' * (len_paded - len(str1)) + str1
    str2 = '0' * (len_paded - len(str2)) + str2
    res = [0] * len_paded
    carry_flag = 0
    i = len_paded - 1
    while i >= 0:
        tmp = int(str1[i]) + int(str2[i]) + carry_flag
        res[i] = tmp % 2
        carry_flag = 1 if tmp >= 2 else 0
        i -= 1
    print(''.join([str(item) for item in res]))


if __name__ == '__main__':
    str1, str2 = input().split()
    add(str1, str2)
