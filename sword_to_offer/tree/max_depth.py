

class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

        
''' 最大深度'''
def max_depth(root):

    if root == None:
        return 0
    return 1 + max(max_depth(root.right), max_depth(root.left))

