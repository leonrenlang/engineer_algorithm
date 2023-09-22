def plus_one(string, j):
    string_list = list(string)
    if string_list[j] == '9':
        string_list[j] = '0'
    else:
        string_list[j] = str(int(string_list[j]) + 1)
    return ''.join(string_list)


def minus_one(string, j):
    string_list = list(string)
    if string_list[j] == '0':
        string_list[j] = '9'
    else:
        string_list[j] = str(int(string_list[j]) - 1)
    return ''.join(string_list)


# 思想：
def open_lock(deadends, target):
    deads = {item for item in deadends}
    visited = set()
    queue = ['0000']
    step = 0
    visited.add('0000')
    while queue:
        size = len(queue)
        for i in range(size):
            tmp = queue.pop(0)
            if tmp in deads:
                continue
            if tmp == target:
                return step
            for j in range(4):
                up = plus_one(tmp, j)
                if not up in visited:
                    queue.append(up)
                down = minus_one(tmp, j)
                if not down in visited:
                    queue.append(down)
        step += 1
    return -1
