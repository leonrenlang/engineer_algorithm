"""
问题： 返回两个链表相交的第一个节点
在本题中，单链表可能有环，也可能无环；这两个链表可能相交，也可能不相交。
要求：如果链表1的长度为N，链表2的长度为M，时间复杂度请达到 O(N+M)，额外空间复杂度请达到O(1)。
"""


# 思路：两个链表相交的节点
# - 两个都是无环的
#   - 思路1：一个全进哈希表，遍历另一个
#   - 思路2：
#       - 分别遍历两个链表，判断两个链表的最后一节点内存地址是否相等，如果不等，则不相交
#       - 如果相等，长的先走len(长) - len(短)，然后一起走，第一个相同节点既是
# - 一个有环一个无环
#   - 不可能相交
# - 两个都有环
#   - 一共可能有三种拓扑结构：两个独立有环链表，在环之前相交，分别指向环上不同节点
#   - 如果loop1 == loop2, 第二种，以loop结尾，就是无环相交问题
#   - 如果loop1 != loop2,loop1一直往下走，如果转回到loop1还没遇到loop2，第一种结构，返回false
#   - 否则,第三种结构，随便返回loop1或者loop2


# 主函数
def linklist_crosspoint(head1, head2):
    if not head1 or not head2:
        return None
    loop1 = get_loop_node(head1)
    loop2 = get_loop_node(head2)
    if not loop1 and not loop2:
        return no_loop_crosspoint(head1, head2)
    elif loop1 and loop2:
        return both_loop_crosspoint(head1, loop1, head2, loop2)
    return None


# 两个都无环的情况
def no_loop_crosspoint(head1, head2):
    p1, p2 = head1, head2
    length_diff = 0
    while p1.next:
        p1 = p1.next
        length_diff += 1
    while p2.next:
        p2 = p2.next
        length_diff -= 1
    if p1 != p2:
        return None
    p1 = head1 if length_diff > 0 else head2  # p1是长的
    p2 = head1 if p1 == head2 else head2
    for _ in range(abs(length_diff)):
        p1 = p1.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


def no_loop_crosspoint2(head1, head2):
    p1 = head1
    p2 = head2
    while p1 != p2:
        if not p1.next and not p2.next:
            return None
        p1 = p1.next if p1.next else p2
        p2 = p2.next if p2.next else p1
    return p1


# 两个都有环的情况
def both_loop_crosspoint(head1, loop1, head2, loop2):
    if loop1 == loop2:
        # 代码参考no_loop_cross
        pass
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1
            cur1 = cur1.next
        return None


# 问题：链表是否有环，并且返回环的初始节点

# 思路1：使用hash表
def get_loop_node1(head):
    cur = head
    table = {}
    while cur:
        if cur not in table.keys():
            table[cur] = 1
        else:
            return cur
        cur = cur.next
    return None


# 思路2：
# - 准备两个指针，快指针一次走两步，慢一次走一步，如果快遇到空了，直接返回无环
# - 如果有环，两个指针一定会在环中相遇，相遇时快指针回到入环节点处，然后一次走一步
# - 两个指针一定会在入环节点初相遇
def get_loop_node2(head):
    if not head or head.next or head.next.next:
        return None
    slow, fast = head.next, head.next.next

    while slow != fast:
        if not fast.next or not fast.next.next:
            return None
        slow = slow.next
        fast = fast.next.next

    while slow != fast:
        if not fast.next or not fast.next.next:
            return None
        slow = slow.next
        fast = fast.next.next

    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

