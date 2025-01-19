
# 删除节点

# 1. 没有头节点的情况

    #1.1原地删除,适合非尾节点
    node.val = node.next.val 
    node.next = node.next.next

    # 1.2跳过删除，适合非头节点
    pointer.next = pointer.next.next

    # 1.3还要考虑只有一个节点的情况，那么就要直接把链表删掉

# 2. 有头节点的情况，那么直接
    pointer.next = pointer.next.next


'''
3.给定值不同的影响
    - 3.1如果给定的是要被删除的节点
        使用原地删除，并且要处理只有一个节点，和尾节点的情况，时间复杂度O(1)
    - 3.2如果给定是要被删除的节点的值（值唯一）
        如果只有一个节点，判断值，删除
        如果是，原头节点地删除
        如果是其他节点pointer.next = pointer.next.next
        代码：
            def deleteNode(self, head: ListNode, val: int) -> ListNode:
                if head.val == val:
                    if head.next == None:
                        return None
                    else:
                        head.val = head.next.val
                        head.next = head.next.next
                        return head
                pointer = head
                while pointer.next.val != val:
                    pointer = pointer.next
                pointer.next = pointer.next.next
                return head               
    - 3.3给定的是倒数第n个数
        双指针找到倒数第n个数，删除
'''

