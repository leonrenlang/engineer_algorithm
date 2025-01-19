class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

# 思路1：使用hash表的方法
# 先复制链表，顺序构造新老链表对应的哈希表，然后
# 根据哈希表给新链表加上ramdom.
class Solution:
    def copy_comples_list(self, head: 'Node') -> 'Node': 
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
            if p1.random: # 如果不存在那么没有对应的hash值
                p2.random = note_hash[p1.random]
            p1 = p1.next
            p2 = p2.next
        return new_head


# 思路2：
# 1.在原链表上复制每一个节点
# 2.复制每一个节点的random
# 3.拆分链表
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        original = head
        while head:#合并两个链表
            temp = head.next
            node = Node(head.val)
            head.next = node
            node.next = temp
            head = temp
               
        temp_1 = original
        temp_2 = original.next

        while temp_1:# 处理random连接
            if temp_1.random:
                temp_2.random = temp_1.random.next
            else:
                temp_1.random = None
            temp_1 = temp_2.next
            if temp_2.next:
                temp_2 = temp_1.next
            else:
                break
        
        temp_1 = original
        temp_2 = original.next
        result = temp_2

        while temp_1:#拆分链表
            temp_1.next = temp_2.next
            temp_1 = temp_2.next
            if temp_2.next:
                temp_2.next = temp_1.next
                temp_2 = temp_1.next
            else:
                temp_2.next = None
         
        return result
    
    # 待补完
    def copy_comples_list(self, head):

        p1 = head
        while p1:
            node = Node(p1.val)
            node.next = p1.next
            p1.next = node
            p1 = node.next

        p1 = head
        p2 = None
        while p1:
            p2 = p1.next
            if p1.random:
                p2.random = p1.random.next
            p1 = p2.next
            
        p1 = head    # 拆分链表
        p2 = head.next
        res = p2
        while p1:
            p1.next = p2.next
        
