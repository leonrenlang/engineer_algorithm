class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



# 无论哪种遍历打印，本质上都是DFS
# 无论是递归还是非递归，遍历一棵树的时间复杂度都是O(n), 空间复杂度都是O(L), L是二叉树的层数

def traversal_preorder(root):
    '''
        递归考虑两种情况即可，抽象情况和边界情况
    '''
    if not root: return
    print(root.value)
    traversal_preorder(root.left)
    traversal_preorder(root.right)


def traversal_inorder(root):
    if not root: return
    traversal_inorder(root.left)
    print(root.value)
    traversal_inorder(root.right)


def traversal_postorder(root):
    if not root: return
    traversal_postorder(root.left)
    traversal_postorder(root.right)
    print(root.value)


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    # head.left.left.left = TreeNode(8)
    # head.left.left.right = TreeNode(9)
    # head.left.right.left = TreeNode(10)
    # head.left.right.right = TreeNode(11)
    # head.right.left.left = TreeNode(12)
    # head.right.left.right = TreeNode(13)
    # head.right.right.left = TreeNode(14)
    # head.right.right.right = TreeNode(15)
    lever_order(head)
