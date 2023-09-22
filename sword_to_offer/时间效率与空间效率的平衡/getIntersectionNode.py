
# 两个链表的第一个公共节点
# 思路：
# 我们使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，
# 然后同时分别逐结点遍历，当 node1 到达链表 headA 的末尾时，重新定位到链表 headB 的头结点；
# 当 node2 到达链表 headB 的末尾时，重新定位到链表 headA 的头结点。

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB      #注意，使用的是if node1,而不是if node1.next
            node2 = node2.next if node2 else headA      #当两个链表不存在交叉节点时，都是None,也能跳出循环
        return node1

   
        
