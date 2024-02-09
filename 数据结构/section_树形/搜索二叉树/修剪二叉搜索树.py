class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思想：
# - 当 \text{node.val > R}node.val > R，那么修剪后的二叉树必定出现在节点的左边。
# - 类似地，当 \text{node.val < L}node.val < L，那么修剪后的二叉树出现在节点的右边。
# - 否则，我们将会修剪树的两边。
# - 时间复杂度O(N), 空间复杂度O(N)(当树的节点数等于其深度）
def trimBST(root, L, R):
    if not root: return None
    if root.val > R:
        return trimBST(root.left, L, R)
    elif root.val < L:
        return trimBST(root.right, L, R)
    else:
        root.left = trimBST(root.left, L, R)
        root.right = trimBST(root.right, L, R)
        return root


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(0)
    head.right = TreeNode(2)
    # head.left.left = TreeNode(7)
    # head.left.right = TreeNode(9)
    # head.right.left = TreeNode(25)
    # head.right.right = TreeNode(37)

    # head.left.left.left = TreeNode(8)
    # head.left.left.right = TreeNode(9)
    # head.left.right.left = TreeNode(10)
    # head.left.right.right = TreeNode(11)
    # head.right.left.left = TreeNode(12)
    # head.right.left.right = TreeNode(13)
    # head.right.right.left = TreeNode(14)
    # head.right.right.right = TreeNode(15)
    Solution().trimBST(head, 1, 2)
