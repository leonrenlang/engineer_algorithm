

# 从上到下，从左到右打印二叉树(中序遍历)
def level_order(root):
    if not root: return []
    queue = [root]
    result = []
    while queue:
        for _ in range(len(queue)):
            item = queue.pop(0)
            result.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
    return result

# 从上到下，从左到右打印二叉树, 每一层打印到一行。
def level_order(root):
    if not root: return []
    queue = [root]
    result = []
    while queue:
        tmp = []
        # 这一句是精华，给每一层画清楚了边界
        for _ in range(len(queue)):
            item = queue.pop(0)
            tmp.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        result.append(tmp)
    return result

# 之字形顺序打印二叉树
def levelOrder(root):
    if not root: return []
    res, queue = [], [root]
    while queue:
        tmp = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        # 先判断是否需要旋转，然后再加进去
        res.append(tmp[::-1] if len(res) % 2 else tmp)
    return res


