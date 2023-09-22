class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 问题：目前我们的数据结构都是在内存中，如果想将树存在硬盘中，则需要序列化
# 如果这个序列化的格式是很好键入的，则可以用其反序列方法构造二叉树


# 不同的序列化方法其实是保存在硬盘中的二叉树的格式的不同。

# ------使用先序(DFS)遍历序列化------

# 思想：假设左右子树已经序列化了，将当前节点的序列化字符串与左右子树序列化字符串拼接
# base case: 假设为空节点，则返回特定的占位字符串
def serialize_by_pre(head):
    if not head: return '#!'  # 如果base case直接返回空字符串，那么在反序列化的时候，就分不清左右孩子了
    cur = str(head.val) + '!'  # 加！的目的是放歧义，如果一个节点的值为12，需要区别其为一个节点，还是两个节点
    res_left = serialize_by_pre(head.left)
    res_right = serialize_by_pre(head.right)
    return cur + res_left + res_right


def recover_by_prestring(string):
    # 反序列化
    def process(values):
        # base case
        if len(values): return None
        value = values.pop(0)
        if value == '#':
            return None
        head = TreeNode(int(value))
        head.left = process(values)

        head.right = process(values)

        return head

    values = string.split('!')
    return process(values)


# -------层序(BFS)遍历序列化------
# 思想：在层序遍历的基础上，入队的时候序列化，因为空节点并不入队，因此出队的时候就没了
def level_order_serialize(head):
    if not head: return '#!'
    res = str(head.val) + '!'
    queue = [head]
    while queue:
        tmp = queue.pop(0)
        if tmp.left:  # 应该在进队的时候判断，因为出队时判断就没有空节点了。
            res += (str(tmp.left.val) + '!')
            queue.append(tmp.left)
        else:
            res += '#!'
        if tmp.right:
            res += (str(tmp.right.val) + '!')
            queue.append(tmp.right)
        else:
            res += '#!'
    return res


# 思想：层序遍历，刚开始树并不存在，但是假设树存在，在判断当前子树的子结点是否应该入队之前，
# 将它们构建出来
def recover_by_levelstring(string):
    def gen_node(value=None):
        if value != '#':
            return TreeNode(int(value))
        else:
            return None

    values = string.split('!')[:-1]
    head = gen_node(values[0])
    queue = [head]
    idx = 1
    while queue:  # 要保证values中每个数都判断一次，且能建树
        node = queue.pop(0)
        node.left = gen_node(values[idx])
        idx += 1
        node.right = gen_node(values[idx])
        idx += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return head



def func():

    queue = [head]
    idx = 1
    while queue:
        node = queue.pop(0)

# ------工具------
def lever_order_print(head):
    # 层序打印一棵树
    if not head: return
    queue = [head]
    while queue:
        tmp = queue.pop(0)
        print(tmp.val)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)


if __name__ == "__main__":
    # head = TreeNode(1)
    # head.left = TreeNode(2)
    # head.right = TreeNode(3)
    # head.left.left = TreeNode(4)
    # head.left.right = TreeNode(5)
    # head.right.left = TreeNode(6)
    # head.right.right = TreeNode(7)
    # serialze_str = level_order_serialize(head)
    # print(serialze_str)
    # head = recover_by_levelstring(serialze_str)
    # lever_order_print(head)

    string = '1!20!30!#!50!#!#!#!#!'
    head = recover_by_levelstring(string)
    lever_order_print(head)
