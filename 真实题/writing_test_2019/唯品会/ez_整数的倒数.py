# 题目描述
# 整数的倒数
# 输入描述:
# 输入一个整数x
# 输出描述:
# 把x倒序输出
# 示例1
# 输入
# 复制
# 123
# 输出
# 复制
# 321
# 示例2
# 输入
# 复制
# -123
# 输出
# 复制
# -321
# 示例3
# 输入
# 复制
# -0
# 输出
# 复制
# -0


def process(num):
    if num[0] == '-':
        content = num[1:]
        return '-' + content[::-1]
    else:
        return num[::-1]


if __name__ == '__main__':
    num = str(input())
    print(process(num))
