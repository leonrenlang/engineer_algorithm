# 给定一个字符串str,将其中所有的空格字符替换成"%20"
# 假设str后面足够的空间

# 思想：
# - 替换的问题在于不知道目标字符的个数，如果从前往后替换
# 就需要反复移动一些字符
# - 解决方法是先计算目标字符的个数，从后往前将数据贴上去


def process(string, aim_ch=' ', substitude='%20'):
    num_aim_ch = 0
    for char in string:
        if char == aim_ch:
            num_aim_ch += 1
    len_res = len(string) + num_aim_ch * (len(substitude) - 1)
    res = [0] * len_res
    idx = len(res) - 1
    for i in range(len(string) - 1, -1, -1):
        item = string[i]
        if item != aim_ch:
            res[idx] = item
            idx -= 1
        else:
            res[idx - 2:idx + 1] = '%20'
            idx -= 3
    return ''.join(res)


if __name__ == '__main__':
    string = 'a b c'
    print(process(string))
