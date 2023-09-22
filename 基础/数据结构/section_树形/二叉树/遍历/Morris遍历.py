class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 目的：
# - 时间复杂度O(N)，空间复杂度O(1)

# 为什么能够实现？
# - 有些节点的指针指向空，其浪费了空间（python好像没有浪费空间），
# 可以利用这些空间完成遍历

# 思想：
# - 如果一个节点有左子树，则会到达该节点两次，如果没有，则只会到达一次
# 而且第二次到达的时候，左子树已经遍历完了
# - 其用左子树最右的这个节点指向谁，来判断我是第几次来到当前节点

# 过程：
# 1. 来到的当前节点记作cur(引用），如果cur无左孩子，cur向
# 右移动（cur = cur.right)
# 2. 如果cur有左孩子，找到cur左子树最右的节点，记为mostright
# - 如果mostright的right指针指向空，让其指向cur,cur向左移动
# - 如果mostright的right指向cur，让其指回空，cur向右移动


def traversal_morris_inorder(head):
    if not head: return None
    cur = head
    while cur:
        most_right = cur.left
        if most_right:
            while most_right.right and most_right.right != cur:  # 找到真的most_right
                most_right = most_right.right
            if not most_right.right:  # 第一次来到当前节点
                most_right.right = cur
                cur = cur.left
                continue
            elif most_right.right == cur:  # 第二次来到当前节点
                most_right.right = None
        print(cur.val)  # 处理完左子树，打印
        cur = cur.right


def traversal_morris_preorder(head):
    if not head: return None
    cur = head
    while cur:
        most_right = cur.left
        if most_right:
            while most_right.right and most_right.right != cur:  # 找到真的most_right
                most_right = most_right.right
            if not most_right.right:  # 第一次来到当前节点
                most_right.right = cur
                print(cur.val)  # 有左子树，第一次来到自己时打印
                cur = cur.left
                continue
            elif most_right.right == cur:  # 第二次来到当前节点
                most_right.right = None
        else:
            print(cur.val)  # 节点压根没有左子树，第一次和第二次回到自己相同
        cur = cur.right


# Morris后序遍历：
# - 只关注能够达到两次的结点，在第二次到达的时候，打印其most_right
# - 整个函数退出之前，单独打印整颗树的右边界
def reverseEdge(node):
    pre = None
    while node:
        nex = node.right
        node.right = pre
        pre = node
        node = nex
    return pre


def print_edge(node):
    tail = reverseEdge(node)
    cur = tail
    while cur:
        print(cur.val)
        cur = cur.right
    reverseEdge(tail)


def traversal_morris_posorder(head):
    if not head: return None
    cur = head
    while cur:
        most_right = cur.left
        if most_right:
            while most_right.right and most_right.right != cur:  # 找到真的most_right
                most_right = most_right.right
            if not most_right.right:  # 第一次来到当前节点
                most_right.right = cur
                cur = cur.left
                continue
            elif most_right.right == cur:  # 第二次来到当前节点
                most_right.right = None
                print_edge(cur.left)
        cur = cur.right
    print_edge(head)


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    # head.left.left.left = TreeNode(8)
    # head.left.left.right = TreeNode(9)
    # head.left.right.left = TreeNode(10)
    # head.left.right.right = TreeNode(11)
    # head.right.left.left = TreeNode(12)
    # head.right.left.right = TreeNode(13)
    # head.right.right.left = TreeNode(14)
    # head.right.right.right = TreeNode(15)
    traversal_morris_posorder(head)
