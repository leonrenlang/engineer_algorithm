


# 输入前序和中序遍历结果，重建二叉树

def buildTree(preorder, inorder):

    if len(inorder) == 0:
        return None
    root = TreeNode(preorder[0])
    mid_idx = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid_idx+1], inorder[:mid_idx])
    root.right = buildTree(preorder[mid_idx+1:],inorder[mid_idx+1:])
    return root
    