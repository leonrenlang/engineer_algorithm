# 给你一个树，请你 按中序遍历 重新排列树，中序遍历第一个节点作为新树的根，其后每一个节点依次接在其父的右子树上
# 每个结点没有左子结点，只有一个右子结点。
# 示例 ：
# 输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \
# 1        7   9
#
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root):
        def process(node):
            if not node: return
            process(node.left)  # 先把左边处理了，此时self.cur为左子树最后一个节点
            node.left = None
            self.last.right = node  # 把左子树最后一个节点指向当前节点
            self.last = node  # 记录该节点
            process(node.right)  # 处理右子树

        self.last = TreeNode(None)
        ans = self.last
        process(root)
        return ans.right
