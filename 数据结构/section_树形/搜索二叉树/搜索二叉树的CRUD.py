class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 查找/修改（对于键值对类数据查找和修改是一样的)
def search(root, target):
    while root and root.val != target:
        if root.val > target:
            root = root.left
        else:
            root = root.right
    return root


# 插入
def insert(root, target):
    if not root:
        root = TreeNode(target)
        return root
    insert_parent_node = None
    while root:
        insert_parent_node = root
        if root.val > target:
            root = root.left
        else:
            root = root.right
    new_node = TreeNode(target)
    if target > insert_parent_node.val:
        insert_parent_node.right = new_node
    else:
        insert_parent_node.left = new_node
    return new_node


# 删除
# - 如果要删的结点没有左子树或者没有右子树，将该节点的子树交给其父亲
# - 如果要删的结点儿女双全，将其右子树的最左结点（左子树的最右）代替它
def delete(element):
    def process():
        pass
