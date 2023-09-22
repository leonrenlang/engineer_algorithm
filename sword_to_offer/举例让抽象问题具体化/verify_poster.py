

# 判断一个序列是否是一棵二叉搜索树的后续遍历
# 思路：后续遍历一定是【左子树 右子树 根节点】

class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            l = i
            while postorder[l] < postorder[j]: l += 1
            m = l
            while postorder[l] > postorder[j]: l += 1
            return l == j and recur(i, m - 1) and recur(m, j - 1)

        # 当需要给子问题输入指针的时候，一般需要辅助函数
        return recur(0, len(postorder) - 1)
