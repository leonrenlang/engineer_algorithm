# 问题：将二叉树改造成二叉树的镜像
# 对于每个根节点来说，左边改造完到右边，右边改造完到左边
# 后序遍历


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
