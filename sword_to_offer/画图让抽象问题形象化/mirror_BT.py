

# 将二叉树改造成二叉树的镜像
# 对于每个根节点来说，左边改造完到右边，右边改造完到左边
# 后序遍历


def mirrorTree(root):
    if root:
        root.left, root.right = mirrorTree(root.right), mirrorTree(root.left)
    return root

    