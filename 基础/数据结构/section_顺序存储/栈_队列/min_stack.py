"""
问题：实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
1．pop、push、getMin操作的时间复杂度都是O(1)。
2．设计的栈类型可以使用现成的栈结构。 
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, num):
        self.stack.append(num)
        if self.min_stack[-1] > num or not self.min_stack:
            self.min_stack.append(num)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if len(self.stack) == 0:
            print('The stack is empty')
        else:
            self.min_stack.pop()
            return self.stack.pop()

    def min(self):
        if len(self.stack) == 0:
            print('The stack is empty')
        else:
            return self.min_stack[-1]

    def top(self):
        if len(self.stack) == 0:
            print('The stack is empty')
        else:
            return self.stack[-1]
