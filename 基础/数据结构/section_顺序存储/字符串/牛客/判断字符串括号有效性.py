# 给定一个字符串，判断是不是整体有效的括号字符串


# - 因为括号的类型是有限的，可以不用栈
# - 用一个整型变量代表'(' 出现次数与')'出现次数的差值
# - 遍历的过程中如果遇到'(’，则num += 1,')'， 则num-=1
# - 遍历的过程如果num < 0，则直接返回False
# - 如果结束num不为0,则返回False

def process(string):
    num = 0  # 用于指示括号数目

    for item in string:
        if item == '(':
            num += 1
        elif item == ')':
            num -= 1
        if num < 0: return False
    return True if num == 0 else False


if __name__ == '__main__':
    pass
