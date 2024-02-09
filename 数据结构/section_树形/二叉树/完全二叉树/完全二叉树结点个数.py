class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ----------------问题：求完全二叉树节点的个数------------------------
# 要求：时间复杂度低于O(N)，N为这棵树的节点个数
# 思想：
# - 由于要求复杂度低于O(n)，因此不能遍历
#     对于完全二叉树，往左走到底一定是它的高
#     右子树也一样，获取右子树的高度，
#         如果depth(right)+1 == h_total，那么左子树是一棵满二叉树，右子树还是完全二叉树，递归
#         如果depth(right)+1 != h_total, 那么右子树是一棵满二叉树，左子树是完全二叉树，递归
# 算法时间复杂度：O(logn*logn)
#     (重)因为每一层只会对一个节点进行计算


def height_of_tree(head):
    height = 0
    while head:
        height += 1
        head = head.left
    return height


def func(head):
    if not head: return 0
    height_cur = height_of_tree(head)
    height_right = height_of_tree(head.right)
    if height_cur == height_right + 1:
        return pow(2, height_cur - 1) + func(head.right)
    else:
        return func(head.left) + pow(2, height_right)


if __name__ == '__main__':
    head = TreeNode(20)
    head.left = TreeNode(8)
    head.right = TreeNode(30)
    head.left.left = TreeNode(7)
    head.left.right = TreeNode(9)
    head.right.left = TreeNode(25)
    head.right.right = TreeNode(24)
    print(func(head))
