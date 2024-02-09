class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 问题：判断完全二叉树（完全二叉树定义:包括满二叉树，只能最后一层的从右到左少，其他不能少）
# 思想：层序遍历
# - 如果某一个节点左不在，右在，直接返回False
# - 如果某一个节点左在右不在，或者左右都不在，开启判断模式，判断模式下，左右有一个不为空，返回false
def is_complete_BT(root):
    if not root:
        return True
    queue = [root]
    flag = False
    while queue:
        tmp = queue.pop(0)
        if (not tmp.left and tmp.right) or (flag and (tmp.left or tmp.right)):
            return False
        if not tmp.right:  # 这个右不在，包括了左在和左不在两种情况，这两种情况都要开启判断模式
            flag = True
        if tmp.left:  queue.append(tmp.left)
        if tmp.right: queue.append(tmp.right)
    return True


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    tmp = head.left
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    # head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    print(is_complete_BT(head))
