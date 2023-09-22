

# 返回链表中倒数第k个节点
# 思路：快指针先走k步，然后快慢指针同步走，快的走到空了，返回慢的


def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

    pioneer = head
    for i in range(k):
        pioneer = pioneer.next
        
    res_pointer = head
    while pioneer:
        res_pointer = res_pointer.next
        pioneer = pioneer.next

    return res_pointer