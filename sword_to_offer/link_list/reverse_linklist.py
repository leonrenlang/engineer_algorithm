

        
# 利用队列实现迭代算法
def reverse_list(head):
    if not head: return None
    queue = deque()
    while head.next:
        deq.append(head)
        head = head.next
    tmp = head
    while deq:
        node = deq.pop()
        node.next = tmp.next
        tmp.next = node
    return head
        

# 双指针方法：非原地反转，新造了一个链表
def reverse_list(head):
    if not head: return None
    pre = head
    cur = None
    while pre:
        tmp = ListNode(pre.val)
        tmp.next = cur
        cur = tmp
        pre = pre.next
    return cur

    
        