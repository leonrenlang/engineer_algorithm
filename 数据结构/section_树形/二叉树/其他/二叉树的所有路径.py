class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 问题: 给定一个二叉树
def BT_paths(root):
    def process(root, path):
        if not root: return None
        path += str(root.val)
        if not root.left and not root.right:
            paths.append(path)
        else:
            path += '->'
            process(root.left, path)
            process(root.right, path)

    paths = []
    process(root, '')
    return paths


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    res = BT_paths(head)
    print(res)
