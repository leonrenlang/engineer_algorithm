"""
题目：复制含有随机指针节点的链表

进阶：
不使用额外的数据结构，只用有限几个变量，且在时间复杂度为 O(N)
内完成原问题要实现的函数。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


# 思路1：使用hash表
# 遍历原始链表，创建一个包含原始节点和新建节点对的哈希表
# 再遍历一次，将链表的next和random信息加到新建链表上。
def copy_random_list(head):
    if not head: return None
    tabel = {}
    cur = head
    while cur:
        tabel[cur] = Node(cur.val)
        cur = cur.next

    cur = head
    while cur:
        tabel[cur].next = tabel[cur.next]
        if cur.random:
            tabel[cur].random = tabel[cur.random]
        cur = cur.next
    return tabel[head]


# 思路2：
#   - 复制每一个节点
#   - 复制每一个节点的random
#   - 拆分链表
def copy_random_list2(head):
    if not head: return None

    cur = head  # 复制链表
    while cur:
        nex = cur.next
        cur.next = Node(cur.val)
        cur.next.next = nex
        cur = nex

    cur = head  # 给新链表加上random链接
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    cur = head  # 拆分两个链表
    copy_head = head.next  # 保存新链表的头
    while cur:
        nex = cur.next.next
        copy_cur = cur.next
        cur.next = nex
        if nex: copy_cur.next = nex.next
        cur = nex
    return copy_head
