


#  两个链表的第一个公共节点

def get_intersection_node(headA, headB):
    node1, node2 = headA, headB
    while node1 != node2:
        node1 = node1.next if node1 else headB
        node2 = node2.next if node2 else headA
    return node1