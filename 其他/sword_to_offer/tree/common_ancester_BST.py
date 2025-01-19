
#二叉搜索树的最近公共祖先
#思路：对于根节点，如果给定的两个节点分别在我的两边，或者其中
# 一个就是我，那么我就是他们的最低公共祖先
# O(depth)

def lowest_commont_ancester(root, p ,q):
    if (root.val - p.val)*(root.val - q.val) <= 0:
        return root
    if q.val < root.val:
        return lowest_commont_ancester(root.left, p, q)
    else:
        return lowest_commont_ancester(root.right,p,q)