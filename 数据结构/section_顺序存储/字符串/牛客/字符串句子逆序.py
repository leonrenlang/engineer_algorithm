# 给定一个字符串，请在单词间做逆序调整
# eg: “pig loves dog" 逆序成 "dog loves pig"


# 1. 实现能将字符串局部所有字符逆序的函数f
# 2. 找到每个单词区域，进行逆序


def reverse_word(string, left, right):
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1


def process(string):
    string = list(string)
    reverse_word(string, 0, len(string) - 1)

    left = 0
    for idx in range(len(string)):
        if string[idx] == ' ':
            reverse_word(string, left, idx - 1)
            left = idx + 1
    reverse_word(string, left, len(string) - 1)
    return ''.join(string)


if __name__ == '__main__':
    string = 'dog loves pig'
    res = process(string)
    print(res)
