# 返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
#
# (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，
# 值总 < node.val，而 node.right 的任何后代，值总 > node.val。此外，先序遍历首先显示节点的值，
# 然后遍历 node.left，接着遍历 node.right。）
# 示例：
# 输入：[8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])

        if len(preorder) == 1: return root  # 要用到第二个元素的索引, 要保证它存在
        split_point = 1
        # 如果只有左子树的情况,则会出现out of index,要限定split_point的范围
        while split_point < len(preorder) and preorder[split_point] <= preorder[0]:
            split_point += 1

        root.left = self.bstFromPreorder(preorder[1:split_point])
        root.right = self.bstFromPreorder(preorder[split_point:])
        return root


if __name__ == '__main__':
    preorder = [4, 2]
    res = Solution().bstFromPreorder(preorder)
