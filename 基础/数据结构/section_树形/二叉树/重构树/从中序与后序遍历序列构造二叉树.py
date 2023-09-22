class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        inorder_idx = inorder.index(root_val)
        # 切片不会out of index，因此可以不考虑边界条件
        root.left = self.buildTree(inorder[:inorder_idx], postorder[:inorder_idx])
        root.right = self.buildTree(inorder[inorder_idx + 1:], postorder[inorder_idx: -1])
        return root


if __name__ == '__main__':
    inorder = [9]
    postorder = [9]
    res = Solution().buildTree(inorder, postorder)
