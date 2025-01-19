
# 复杂链表的复制

# 使用hash表的方法
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node': 
    
        if not head: return None
        new_head = Node(head.val) 
        p1 = head.next
        p2 = new_head
        note_hash = {head:new_head}
        while p1:
            p2.next = Node(p1.val) 
            p2 = p2.next
            note_hash[p1] = p2
            p1 = p1.next

        p1 = head
        p2 = new_head
        while p1:
            if p1.random:
                p2.random = note_hash[p1.random]
            p1 = p1.next
            p2 = p2.next
        return new_head

# 不需要辅助空间的方法
# 1.复制每一个节点
# 2.复制每一个节点的random
# 3.拆分链表