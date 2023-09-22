
'''判断是否为对称二叉树
   - 关键点在于要让处在对称位置的点一块玩
   - 如果根节点在，判断左右子树是否对称
   - 对于一对子树，如果同时不在，或者都在且右的左和左的右 右的右和左的左对称，那么应该是对称的，否则不对称
'''

def symmetric_tree(left_node, right_node):
    if not left_node and not right_node:
        return True
    if left_node and right_node and left_node.value == right_node.value:
        return symmetric_tree(left_node.left, right_node.right) and 
            symmetric_tree(left_node.right, right_node.left)
    else:
        return False

if not root:
    result = True
result = symmetric_tree(root.left, root.right)




# --------------------------------
class TreeNode():
    def __init__(val):
        self.val = val
        self.left = None
        self.right = None
