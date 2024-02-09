



# 问题3: 别墅现在组成一棵二叉树，房子在二叉树的节点上，相连的两个房子不能被同时抢劫
# 思想：
# - 采用一个字典纪录已经计算过的结点，
# - 这里仍使用了递归是因为数据结构本身是一棵树，遍历二叉树需要递归
def rob(root):
    dic = {}
    def process(root):
        if not root: return 0
        if root in dic.keys():
            return dic[root]
        do_it = root.val \
                + (0 if not root.left else rob(root.left.left) + rob(root.left.right)) \
                + (0 if not root.right else rob(root.right.left) + rob(root.right.right))
        not_do = rob(root.left) + rob(root.right)
        res = max(do_it, not_do)
        dic[root] = res
        return res

    return process(root)


# 一种改进方法，不需要hashmap来保存值了
def rob2(root):
    def dp(root):
        if not root: return 0, 0
        left = dp(root.left)
        right = dp(root.right)
        do_it = root.val + left[0] + right[0]
        not_rob = max(left[0], left[1]) \
                  + max(right[0], right[1])
        return not_rob, do_it

    res = dp(root)
    return max(res[0], res[1])


if __name__ == '__main__':
    arr = [2, 7, 9, 1, 10, 3]
    print(rob(arr))
