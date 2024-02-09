class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思想：尽管前序和后序不能唯一确定一棵树，但是可以找到一棵满足的树
# - 先序遍历第二个节点（左子树的根）是后序遍历左子树遍历的最后一个节点，找到后序遍历左子树最后一个节点的index就知道
# 左子树有多长了
# 例子：
# 前序遍历为：
# (根结点) (前序遍历左分支) (前序遍历右分支)
# 而后序遍历为：
# (后序遍历左分支) (后序遍历右分支) (根结点)
# 例如，如果最终的二叉树可以被序列化的表述为 [1, 2, 3, 4, 5, 6, 7]，那么其前序遍历为 [1] + [2, 4, 5] + [3, 6, 7]，而后序遍历为 [4, 5, 2] + [6, 7, 3] + [1].
# 如果我们知道左分支有多少个结点，我们就可以对这些数组进行分组，并用递归生成树的每个分支。

class Solution:
    def constructFromPrePost(self, pre, post) -> TreeNode:
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root  # 要引用第二个元素,因此需要判断是否有第二个元素
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:1 + L], post[:L])
        root.right = self.constructFromPrePost(pre[1 + L:], post[L:-1])
        return root


if __name__ == '__main__':
    pre = [1, 2, 4, 5, 3, 6, 7]
    post = [4, 5, 2, 6, 7, 3, 1]
    res = Solution().constructFromPrePost(pre, post)
