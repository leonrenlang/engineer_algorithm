def reverse_linklist(head):
    # 翻转单链表
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


def reverse_double_linklist(head):
    # 翻转双向链表
    pre = None
    while head:
        next = head.next
        head.next = pre
        head.last = next  # 相比单向链表，仅增加这一句
        pre = head
        head = head.next
    return pre

def copy_list(head):
    # 复制一个链表
    if not head: return None
    copy_head = Node(head.val)
    p1 = head.next
    copy_rear = copy_head
    while p1:
        node = Node(p1.val)
        copy_rear.next = node
        copy_rear = node
        p1 = p1.next
    return copy_head