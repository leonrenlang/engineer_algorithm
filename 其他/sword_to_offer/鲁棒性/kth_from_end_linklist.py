# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 链表中倒数第k个节点
# 典型的双指针题目，注意判断边界

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        pioneer = head
        pointer = head

        for i in range(k):
            if pioneer.next:
                pioneer = pioneer.next
            else:
                return None
        
        while pioneer:
            pointer = pointer.next
            pioneer = pioneer.next
        return pointer

