class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 问题：判断一棵树是否为搜索二叉树（任何节点的左子树的值比其值小，右子树的值比其值大）


# 思想： 利用搜索二叉树中序遍历递增的性质
def func(head):
    def process(head):
        if not head: return None
        process(head.left)
        res.append(head.val)
        process(head.right)
    res = []
    process(head)
    print(res)
    return res == sorted(res) and len(set(res)) == len(res)  # 判断len是因为题目要求严格大于，不能为等于


# 只用一个变量保存上一个节点节省空间
def func2(root):
    def process(head):
        if not head: return True
        if not process(head.left):
            return False
        nonlocal pre
        if pre.val >= head.val:
            return False
        pre = head
        return process(head.right)

    pre = None  # 必须要定义，声明nonlocal变量需要和外面的变量绑定
    return process(root)


# 思想：搜索二叉树的一个特点就是中序遍历是有序的，这里采用非递归的中序遍历是为了节省空间
def is_BST2(head):
    if not head: return True
    stack = []
    last = -1 * pow(2, 32)
    while stack or head:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            if head.val > last:
                last = head.val
            else:
                return False
            head = head.right
    return True


# 思想： 利用根节点的值划分边界
def fun(root):
    def process(root, min_val, max_val):
        if not root: return True
        if not (min_val < root.val < max_val):
            return False
        return process(root.left, min_val, root.val) and process(root.right, root.val, max_val)

    return process(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    head = TreeNode(20)
    head.left = TreeNode(8)
    head.right = TreeNode(30)
    head.left.left = TreeNode(7)
    head.left.right = TreeNode(9)
    head.right.left = TreeNode(25)
    head.right.right = TreeNode(24)
