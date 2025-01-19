

# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
# 如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。


class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

        
''' 最大深度'''

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))




class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #确实这个就是后序遍历，因为上一题求深度实际上也算后序遍历
        if root == None:  return True

        def depth(root):#一边测深度一边判断
            if root == None:
                return 0, True
            depth_l, bool_l = depth(root.left)#返回子树高度，以及子节点是否满足要求
            if not bool_l:return 0, False#剪枝，第一个返回值不重要
            depth_r, bool_r = depth(root.right)
            if not bool_r:return 0, False#剪枝，第一个返回值不重要
            now = False#标记当前节点是否满足
            if -1<=depth_l-depth_r<=1:
                now = True
            return 1+max(depth_l,depth_r), now#剪枝后 (now and bool_l and bool_r)#剪枝前
        _,res = depth(root)
        return res

