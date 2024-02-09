# 问题：判断树是否为平衡二叉树（任意节点的左右子树高度差不大于1）

# 思想：
# -对于问题f(n),首先要保证左右子树是平衡二叉树，然后要保证左右子树的高度差不大于1
# -base case: 树不存在，是平衡二叉树，高度为0
def is_balance(root):
    def process(root):
        if not root: return 0, True
        depth_l, flag_l = process(root.left)
        if not flag_l:
            return 0, False
        depth_r, flag_r = process(root.right)
        if not flag_r:
            return 0, False
        if abs(depth_l - depth_r) <= 1:
            return 1 + max(depth_l, depth_r), True
        else:
            return 0, False

    _, flag = process(root)
    return flag
