# 思想：
# - 把问题抽象成图，从一个点开始，想四周开始扩散
# - 一般要用到队列，每次将一个节点周围的所有节点加入队列
# 参考：https://mp.weixin.qq.com/s/Xn-oW7QRu8spYzL3B6zLxw
# 参考：https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485134&idx=1&sn=fd345f8a93dc4444bcc65c57bb46fc35&chksm=9bd7f8c6aca071d04c4d383f96f2b567ad44dc3e67d1c3926ec92d6a3bcc3273de138b36a0d9&scene=21#wechat_redirect


# 问题1： 二叉树的最小深度(最小深度是从根节点到最近叶子节点的最短路径上的节点数量）
# 思想：树的BFS就是层序遍历，在层序遍历的基础上
# 保留当前深度的变量，以及判断当前是否应该结束
def min_depth(root):
    if not root: return 0
    queue = [root]
    depth = 1
    while queue:
        size = len(queue)
        for i in range(size):
            tmp = queue.pop(0)
            if not tmp.left and not tmp.right:
                return depth
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
            depth += 1
    return depth
