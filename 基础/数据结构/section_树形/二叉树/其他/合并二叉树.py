class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 给定两个二叉树，将他们的对应位置的值加起来
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1: return t2
        if not t2: return t1
        root = TreeNode(0)
        root.val = root.val + t1.val + t2.val
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root


if __name__ == '__main__':
    Solution().mergeTrees()
