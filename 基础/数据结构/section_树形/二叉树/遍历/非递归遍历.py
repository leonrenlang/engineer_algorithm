class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 非递归先序打印  
# 思想：
# - 先序打印的顺序是根、左、右，根节点在第一次遇见的时候就打印
# 然后就得取左边了，因此，需要将右节点（子树)保存在栈中
# - 将左节点(不是子树)保存到栈中,下一个就处理它了，为了不写重复代码
def preorder_unrecur(head):
    if not head: return None
    stack = [head]
    while stack:
        tmp = stack.pop()
        print(str(tmp.val) + ' ')
        if tmp.right: stack.append(tmp.right)
        if tmp.left: stack.append(tmp.left)


# 思想：
# - 对于当前节点，先把自己打印出来，如果右边存在，则把右边保存入栈
# - 尝试去左边节点，如果没有左边，则从栈弹出一个，如果都没有，则结束了
def preorder_print(head):
    cur = head
    stack = []
    while cur:
        print(cur.val)
        if cur.right: stack.append(cur.right)
        if cur.left:
            cur = cur.left
        elif stack:
            cur = stack.pop()
        else:
            break


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    # preorder_print(None)


# 思想：
# - 中序遍历的过程是左、中、右，因此在经过根的时候，不能立刻遍历，应该入栈
# 直到根没有左孩子，也因此不能将第一个根节点在循环外面入栈
def inorder_unrecur(head):
    if not head: return None
    stack = []
    while stack or head:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            print(str(head.val) + ' ')
            head = head.right


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)


# 思想：
# - 后序需要左右中， 反过来就是中右左，先将先序改成中右左
# - 在每次需要输出的时候放入另一个栈中，翻过来即为后序


def func(root):
    cur = root
    stack = []
    res = []
    while cur:
        res.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            cur = cur.right
        elif stack:
            cur = stack.pop()
        else:
            break

    for item in reversed(res):
        print(item)


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    func(head)
