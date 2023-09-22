"""
将单向链表按某值划分成左边小、中间相等、右边大的形式
    
【题目】 给定一个单向链表的头节点head，节点的值类型是整型，再给定一个
整 数pivot。实现一个调整链表的函数，将链表调整为左部分都是值小于 pivot
的节点，中间部分都是值等于pivot的节点，右部分都是值大于 pivot的节点。

除这个要求外，对调整后的节点顺序没有更多的要求。 例如：链表9->0->4->5-
>1，pivot=3。 调整后链表可以是1->0->4->9->5，也可以是0->1->9->5->4。总
之，满 足左部分都是小于3的节点，中间部分都是等于3的节点（本例中这个部
分为空），右部分都是大于3的节点即可。对某部分内部的节点顺序不做要求。
//暗示可以转数组做

进阶： 在原问题的要求之上再增加如下两个要求。
在左、中、右三个部分的内部也做顺序要求，要求每部分里的节点从左 到右的顺序与原链表中节点的先后次序一致。 
如果链表长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)。
//用链表做
"""

"""  
思路:
- 第一遍遍历，分别找到链表中的第一个小于，等于和大于pivot的链表，用指针记录下来
- 第二次遍历，如果当前节点值小于pivot,接在上述小于pivot指针的后面，同理，等于和大于pivot的值的节点，接在对应的指针后面
- 将三个小链表连接起来
"""


def list_partition_1(head, pivot):
    small_head, small_tail = None, None
    equal_head, equal_tail = None, None
    bigger_head, bigger_tail = None, None

    while head:  # every node distributed to three lists

        tmp = head.next
        head.next = None  # 注意要把每个节点的next设为None,因为尾节点不应该有下一个

        if head.val < pivot:
            if not small_head:
                small_head, small_tail = head, head
            else:
                small_tail.next = head
                small_tail = small_tail.next
        elif head.val == pivot:
            if not equal_head:
                equal_head, equal_tail = head, head
            else:
                equal_tail.next = head
                equal_tail = head
        else:
            if not bigger_head:
                bigger_head, bigger_tail = head, head
            else:
                bigger_tail.next = head
                bigger_tail = head

        head = tmp

    if small_tail:
        if equal_tail:
            small_tail.next = equal_head
            equal_head.next = bigger_head
            return small_head
        else:
            small_tail.next = bigger_head
            return small_head
    else:
        if equal_head:
            equal_head.next = bigger_head
            return equal_head
        else:
            return bigger_head
