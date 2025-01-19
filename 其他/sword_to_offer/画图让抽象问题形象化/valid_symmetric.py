
'''判断是否为对称二叉树
   - 关键点在于要让处在对称位置的点一块玩
   - 如果根节点在，判断左右子树是否对称
   - 对于一对子树，如果同时不在，或者都在且右的左和左的右 右的右和左的左对称，那么应该是对称的，否则不对称
'''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if left and right and left.val == right.val:
                return helper(left.left, right.right) and helper(left.right, right.left)
            else:
                return False
        if not root:
            return True
        else:
            return helper(root.left, root.right)

