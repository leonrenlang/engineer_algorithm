
# 二叉树的最近公共祖先

# 情况1：如果右子树找不到 p 或 q 即(right==null)，那么说明 p 和 q 都在左子树上，返回 left
# 情况2：如果左子树找不到 p 或 q 即(left==null)，那么说明 p 和 q 都在右子树上，返回 right
# 情况3：如果上述情况都不符合，说明 p 和 q 分别在左子树和右子树，那么当前节点即为最近公共祖先，直接返回 root 即可。



def lowest_common_ancester(root, p, q):
    if not root:
        return root
    if root.val == p.val or root.val == q.val:
        return root
    l = lowest_common_ancester(root.left, p, q)
    r = lowest_common_ancester(root.right, p, q)     
    return root if l and r else l or r


    