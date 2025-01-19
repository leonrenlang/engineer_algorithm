

'''验证二叉搜索树
    - 对于每一个节点，如果为None，返回True
    - 如果节点的值没在爸爸给的范围内，返回False
    - 该节点验证通过，验证子节点，将本节点将给孩子划定范围
'''

def valid_BST(root, min, max):
    if root == None:
        return True
    if root.val <= min or root.val >= max:
        return False
    return valid_BST(root.left, min, root.val) and valid_BST(root.right, root.val, max)

import sys
min = sys.maxsize * (-1)
max = sys.maxsize
result =  valid_BST(root, min, max)


