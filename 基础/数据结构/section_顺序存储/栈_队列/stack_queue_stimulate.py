# 如何仅用队列结构实现栈结构？
# 如何仅用栈结构实现队列结构？


# 用队列模拟栈
# 思想：
#   队列不会改变数据的顺序。
#   进栈，正常放到队尾；
#   出栈，将队列前n-1个元素都放到另一个队列中，最后一个输出，然后将两个队列交换；
#   获取队头元素，与出栈同，只是不用pop掉队尾元素
class two_queue_stack:

    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, num):
        self.data.append(num)

    def pop(self):
        if not self.data:
            print('stack is empty!')
        while len(self.data) > 1:  # 将self.data队列中除了最后一个都放到helper中
            self.helper.append(self.data.pop(0))
        res = self.data.pop(0)
        self.data, self.helper = self.helper, self.data
        return res

    def top(self):
        if not self.data:
            print('stack is empty!')
        while len(self.data) > 1:
            self.helper.append(self.data.pop(0))
        res = self.data.pop(0)
        self.helper.append(res)
        self.data, self.helper = self.helper, self.data
        return res


# 思想：
# 栈会将输出元素的顺序倒置，而队列的顺序就是数据输入的顺序，因此可以用两个栈模拟队列。
# 进队：进队专用栈
# 出队：如果出队栈有数据，直接出，否则将进队专用栈倒入出队栈
# 获取top：参考出队

class two_stack_queue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, num):
        self.push_stack.append(num)

    def poll(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            if not self.pop_stack:
                print('queue is empty!')
            else:
                return self.pop_stack.pop()
        else:
            return self.pop_stack.pop()

    def top(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            if not self.pop_stack:
                print('queue is empty!')
            else:
                return self.pop_stack[-1]
        else:
            return self.pop_stack[-1]
