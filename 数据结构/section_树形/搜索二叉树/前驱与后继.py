class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# 问题：中序遍历的后继结点，中序结点的前驱结点
# 问题的意义？因为搜索二叉树中序是有序的，所以可以以小于O(n)的时间，找到比当前结点的上一个结点和下一个结点。


# 思想：
# - 某一个节点，假设其左右子树均不为None,那么其前驱即为左子树的最右，其后继则为右子树的最左
# 现在单独考虑后继，如果右子树存在，如上，如果不存在，则把当前节点看做为其父亲的左子树的最右，找其父
# 现在单独考虑前驱，如果左子树存在，如上，如果不存在，则把当前节点看做为其父亲的右子树的最左，找其父
# - 由于需要找到自己的父结点，必须有自己的父指针，如果没有则只能遍历整棵树，找到相应的结点
# 注：一般的算法题中树节点没有父节点，但是实际工程中都会有
def successor(node):
    if not node: return
    if node.right:  # 有右子树的情况
        res = node.right
        while res.left:
            res = res.left
        return res
    else:  # 没有右子树的情况
        while node.parent and node.parent.left != node:
            node = node.parent
        return node.parent


def pioneer(node):
    if not node: return
    if node.left:
        tmp = node.left
        while tmp.left:
            tmp = tmp.left
        return tmp
    else:
        while node.parent and node.parent.right != node:
            node = node.parent
        return node.parent




if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    tmp = head.left
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)


