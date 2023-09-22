class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_idx = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:1 + inorder_idx], inorder[:inorder_idx])
        root.right = self.buildTree(preorder[1 + inorder_idx:], inorder[inorder_idx + 1:])
        return root


