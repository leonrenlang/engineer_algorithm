
# 第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
# 新建一个栈，模拟栈压入弹出过程。
# 如果下一个弹出数字刚好的栈顶数字，那么直接两者都弹出。否则继续压入栈，直到把
# 第一个序列全部压入为止，至此，如果栈仍未完全弹出，则第二个序列并非第一个序列的
# 弹出栈
# 时间复杂度：O(n), 空间复杂度O(n)

class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        while pushed:
            stack.append(pushed.pop(0))
            # 注意，这里用的是while
            while stack and popped and popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop(-1)
        return False if stack else True


