class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 问题：把一段纸条竖着放在桌上，然后从纸条的下方向上方对折一次，压出
# 折痕后展开。给定一个参数N，代表纸条从下向上连续对折N次，请从上到
# 打印所有折痕的方向。

# 思想：
# - 如果是折一次，折痕朝下，如果折两次，在下折痕的两端多出了一道上折痕，和一道下折痕，如果是折三次，在第二次新出现的基础上，左右分别出现一道上折痕，和一道下折痕
# 折N次... 形成一棵树，树的每个节点的左右子树均为上/下折痕
# - 使用类似层序反序列化的方法建树
# - 然后对所建树使用右中左遍历
def func(n):
    def build_tree(values):
        def build_node(value):
            if value == '#':
                return None
            else:
                return TreeNode(value)

        root = build_node(values[0])
        queue = [root]
        idx = 1
        while queue:
            node = queue.pop(0)
            node.left = build_node(values[idx])
            idx += 1
            node.right = build_node(values[idx])
            idx += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    def process(root):
        # 右中左遍历打印树
        if not root: return
        process(root.right)
        res.append(root.val)
        process(root.left)

    values = ['D'] + ['U', 'D'] * ((pow(2, n) - 2) // 2) + ['#'] * pow(2, n)
    root = build_tree(values)
    res = []
    process(root)
    return res

# 递归版本实现上述的build_tree
def build_tree(n):
    def process(val, n):
        # 给定一个val和n返回一个以val为根节点值，n层的树
        if n == 0: return None
        root = TreeNode(val)
        root.left = process('D', n-1)
        root.right = process('U', n-1)
        return root
    tree = process('D', n)
    return tree

print(func(3))
