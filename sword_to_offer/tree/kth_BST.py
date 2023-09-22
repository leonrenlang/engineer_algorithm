
# 二叉搜索树的第k大节点
# if index == 0和if not root是两个出口
# 右中左遍历，找第k个结点

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root: return None
        def in_order(root):
            if not root: return 
            in_order(root.left)
            res.append(root.val)
            in_order(root.right)
        res = []
        in_order(root)
        return res[-k]

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def search_k(root, k):
            if not root:
                return
            search_k(root.right, k)
            K[0] += 1
            if K[0] == k:#当这个第K大的数时,返回
                result[0] = root.val
                return 
            search_k(root.left, k)
        K = [0]#用于计数
        result = [0]#用于保存结果
        search_k(root, k)
        return result[0]
