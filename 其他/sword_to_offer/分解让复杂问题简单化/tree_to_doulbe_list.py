
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
# 思路：中序遍历，对于每个节点，将其左指向上一个节点，将上一个节点指向当前节点
#   保存当前节点为上一个节点
# 注意：这个算法有很多细节
#   1. 为什么self.head, self.pre要放在init中初始化？
#       因为他们的值是None，不是引用
class Solution:
    def __init__(self):
        self.head, self.pre = None, None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:  return None   #防止首尾相接时出错
        def inorder(node):
            if not node: return None
            inorder(node.left) 
            if not self.pre:
                self.head = node #记录初始头节点
            else:
                self.pre.right, node.left = node, self.pre # 按顺序链接节点
            self.pre = node
            inorder(node.right)
        inorder(root)
        # 链接首尾节点
        self.head.left, self.pre.right =  self.pre, self.head 
        return self.head

