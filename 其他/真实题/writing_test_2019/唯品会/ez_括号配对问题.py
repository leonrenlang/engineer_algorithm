# 题目描述
# 括号配对问题
# 输入描述:
# 给定一个字符串S，请检查该字符串的括号是否配对，只含有"[", "]", "(", ")"

# 输出描述:
# 配对，返回true
# 不配对，返回false

# 示例1
# 输入
# abcd(])[efg
# 输出
# false


def judge_bracket(string):
    stack = []
    for item in string:
        if item == '[' or item == '(':
            stack.append(item)
        elif item == ')' or item == ']':
            if len(stack) == 0: return False
            if item == ')' and stack[-1] == '(':
                stack.pop(-1)
            if item == ']' and stack[-1] == '[':
                stack.pop(-1)
    return True if len(stack) == 0 else False


if __name__ == '__main__':
    string = input()
    res = judge_bracket(string)
    if res:
        print('true')
    else:
        print('false')
