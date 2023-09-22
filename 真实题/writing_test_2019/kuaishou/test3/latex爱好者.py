# 题目描述
# latex自然是广大研究人员最喜欢使用的科研论文排版工具之一。
# 月神想在iPhone 上查阅写好的paper，但是无赖iPhone 上没有月神喜欢使用的阅读软件，于是月神也希望像tex老爷爷Donald Knuth那样自己动手do it yourself一个。
# 在DIY这个阅读软件的过程中，月神碰到一个问题，已知iPhone屏幕的高为H，宽为W，若字体大小为S(假设为方形），则一行可放W / S(取整数部分）个文字，一屏最多可放H / S （取整数部分）行文字。
# 已知一篇paper有N个段落，每个段落的文字数目由a1, a2, a3,...., an表示，月神希望排版的页数不多于P页（一屏显示一页），那么月神最多可使用多大的字体呢？
# 1 <= W, H, ai <= 1000
# 1 <= P <= 1000000
# 输入描述:
# 每个测试用例的输入包含两行。
# 第一行输入N,P,H,W
# 第二行输入N个数a1,a2,a3,...,an表示每个段落的文字个数。
# 输出描述:
# 对于每个测试用例，输出最大允许的字符大小S

# 示例1
# 输入
# 1 10 4 3 10 2 10 4 3 10 10
# 输出
# 3 2


import math


# 判断某个字体大小是否符合要求
def judge_fontsize(P, H, W, paras, font_size):
    # 判断一个特定的fontsize是否满足要求
    H = P * H
    row_max = W // font_size
    col_max = H // font_size
    col_need = 0
    for para in paras:
        col_need += math.ceil(para / row_max)
    return True if col_need <= col_max else False


# 二分查找[1,W]之间符合要求的最大的数
def process(P, H, W, paras):
    i = 1
    j = W
    while i <= j:
        m = (i + j) // 2
        if judge_fontsize(P, H, W, paras, m):
            i = m + 1
        else:
            j = m - 1
    print(j)


# 思想：暴力遍历1~W,判断是否符合要求
def process2(P, H, W, paras):
    res = 1
    for i in range(1, W + 1):
        if not judge_fontsize(P, H, W, paras, i):
            print(res)
            return
        else:
            res = i
    print(res)


if __name__ == '__main__':
    N, P, H, W = [int(item) for item in input().split()]
    paras = [int(item) for item in input().split()]
    process(P, H, W, paras)
