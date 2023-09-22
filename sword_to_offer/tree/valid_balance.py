


# 验证平衡二叉树
# 直接思路：
#       左右两颗子树的最大深度的绝对值差<=1, 然后分别验证左右子树，但是有很多重复计算
# 改进思路：
#       采用后续遍历方法，每个节点仅遍历一次
#       因为我们在判断一个节点之前，已经判断了它的左右子树



def depth(root):
    if not root: return 0, True
    depth_l, flag_l = depth(root.left)
    if not flag_l: return 0, False
    depth_r, flag_r = depth(root.right)
    if not flag_r: return 0, False
    
    if abs(depth_l - depth_r) <= 1:
        return 0, False
    else:
        return 1 + max(depth_l,depth_r), True
if not root: return True
_, res = depth(root)
return res


def is_balance(root):
    if not root: return 0, True
    depth_l, flag_l = is_balance(root.left)
    if not flag_l:
         return 0, False
    depth_r, flag_r = is_balance(root.right)
    if not flag_r:
         return 0, False
    if abs(depth_l - depth_r) <= 1:
        return 1 + max(depth_l, depth_r), True
    else:
        return 0, False