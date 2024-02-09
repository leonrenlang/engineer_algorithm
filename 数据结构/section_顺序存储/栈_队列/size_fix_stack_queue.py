# 用数组结构实现大小固定的队列和栈


class Stack:
    # 实现大小固定的栈
    def __init__(self, init_size):
        self.arr = [0] * init_size
        self.index = 0

    def push(self, num):
        if self.index == len(self.arr):
            print('The stack is full')
        else:
            self.arr[self.index] = num
            self.index += 1

    def pop(self):
        if self.index == 0:
            print('The stack is empty')
        else:
            self.index -= 1
            return self.arr[self.index]

    def top(self):
        if self.index == 0:
            print('The stack is empty')
        else:
            return self.arr[self.index - 1]


class Queue:

    def __init__(self, init_size):
        self.arr = [0] * init_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, num):
        if self.size == len(self.arr):
            print('The Queue is full')
        else:
            self.size += 1
            self.arr[self.tail] = num
            self.tail = 0 if self.tail == len(self.arr) - 1 else self.tail + 1

    def pop(self):
        if self.size == 0:
            print('The queue is empty')
        else:
            self.size -= 1
            res = self.arr[self.head]
            self.head = 0 if self.head == len(self.arr) - 1 else self.head + 1
            return res

    def top(self):
        if self.size == 0:
            print('The queue is empty')
        else:
            return self.arr[self.head]

