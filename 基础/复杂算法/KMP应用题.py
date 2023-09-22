# 问题：给一个原始串，只能在后面添加字符，要求生成一个长字符串，包含原始串两次
# 两次的起始位置不同。


# 思想：
# - 计算给定字符串的next数组，多求一位的匹配数
# 例子： abcabc  -> next_arr=[-1,0,0,0,1,0,3]，最后的3是多求的一位
# 既有三个数字可以复用，将前面len(arr) - 3的子串加到原始串末尾即为答案


def func(str1):
    next_arr = [0] * (len(str1) + 1)
    next_arr[0] = -1
    idx = 2
    cn = 0
    while idx < (len(str1) + 1):
        if str1[idx - 1] == str1[cn]:
            cn += 1
            next_arr[idx] = cn
            idx += 1
        elif cn > 0:
            cn = next_arr[cn]
        else:
            next_arr[idx] = 0
            idx += 1
    return str1 + str1[:(len(str1) - next_arr[-1])]


str1 = 'abcabc'
print(func(str1))
