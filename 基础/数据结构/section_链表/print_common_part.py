"""
打印两个有序链表的公共部分, 这里的公共部分指的是值相同的部分，不是共享的部分
【题目】 给定两个有序链表的头指针head1和head2，打印两个
链表的公共部分。
"""


def print_common_part(l1, l2):
    p1, p2 = l1, l2
    while p1 and p2:
        if p1.val > p2.val:
            p2 = p2.next
        elif p1.val < p2.val:
            p1 = p1.next
        else:
            print(str(p1.val) + ' ')
            p1, p2 = p1.next, p2.next
