# 问题：
# 给定一棵二叉树，你需要计算它的直径长度。
# 一棵二叉树的直径长度是任意两个结点路径长度中的最大值，路径长度指
# 两个节点之间的边的条数。这条路径可能穿过也可能不穿过根结点。

# 示例 :
# 给定二叉树
#
#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。


# -对于根节点来说，直径为左右深度之和
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def process(root):
            if not root:
                return 0
            L = process(root.left)  # L为左子树的深度
            R = process(root.right)  # R为右子树的深度
            depth = max(L, R) + 1
            self.ans = max(self.ans, L + R)  # 这里要用max，因为是有可能存在子树的直径大于原树的直径的情况的
            return depth

        self.ans = 0
        process(root)
        return self.ans

