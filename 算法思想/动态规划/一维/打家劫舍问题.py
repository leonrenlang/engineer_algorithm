# 问题：有一排别墅，一个小偷需要选择偷哪些住户，能偷到的钱最多
# 不能偷相邻的住户，因为会触发报警。求能偷的的最多的钱

# 思想：
# - dp[i]指的是当前房子向左所有房子的最大收益
# - dp[0]就是当前房子的收益
# - dp[1]的 max(d[0], d[-1]+当前房子的收益)
# -base case，没有房子了，收益为0， 只有一栋房子，那就是这栋房子的收益
def house_robber(nums):
    # 假设最左侧房子左边还存在两座虚拟房子,他们的dp均为0
    dp_i_2, dp_i_1 = 0, 0
    for item in nums:
        dp_cur = max(dp_i_1, dp_i_2 + item)
        dp_i_2 = dp_i_1
        dp_i_1 = dp_cur
    return dp_i_1


# 问题2：仍是一排别墅，但是为环形的
# 思路：
# - 考虑首尾两栋房子，不可能两者都选，可以选择两者其中一个，或者两者都不选
# - 如果两者只选其中一个，由于空缺了一个，首位不再互相印象
# - 两者都不选的结果肯定要小于等于两者中选择一个，因为选择一个的问题规模要大于两者都不选择
#       选择一个的子问题首位不固定即可包含两者都不选的情况。
# - 因此问题变成了在首位各选一个的两个问题的横排数组问题
def house_robber2(nums):
    def process(nums):
        dp_i_2, dp_i_1 = 0, 0
        for item in nums:
            tmp = max(dp_i_1, dp_i_2 + item)
            dp_i_2 = dp_i_1
            dp_i_1 = tmp
        return dp_i_1
    return max(process(nums[:-1]), process(nums[1:])) if len(nums) != 1 else nums[0]


# 问题3: 别墅现在组成一棵二叉树，房子在二叉树的节点上，相连的两个房子不能被同时抢劫
# 思想：
# 
'''
    - 根节点上的最大收益dp[root] = max(not_do, do)
        --not_do = dp[left] + dp[right]
        --do = root.val + dp[left.left] + dp[left.right] + dp[left.left] + dp[left.right]
'''

# - 采用一个字典纪录已经计算过的结点，
# - 这里仍使用了递归是因为数据结构本身是一棵树，遍历二叉树需要递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rob(root):
    def process(root):
        # 该函数返回以root为根可能的最大收益，并且利用一个字典记录其他根的情况
        if not root: return 0
        if root in dic.keys():
            return dic[root]
        do_it = root.val \
                + (0 if not root.left else process(root.left.left) + process(root.left.right)) \
                + (0 if not root.right else process(root.right.left) + process(root.right.right))
        not_do = process(root.left) + process(root.right)
        res = max(do_it, not_do)
        dic[root] = res
        return res
    dic = {}
    return process(root)


if __name__ == '__main__':
    # [3,2,3,null,3,null,1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = 3
    root.right.right = 1
    print(rob(root))

#
# # 一种改进方法，不需要hashmap来保存值了
# def rob2(root):
#     def dp(root):
#         if not root: return 0, 0
#         left = dp(root.left)
#         right = dp(root.right)
#         do_it = root.val + left[0] + right[0]
#         not_rob = max(left[0], left[1]) \
#                   + max(right[0], right[1])
#         return not_rob, do_it
#
#     res = dp(root)
#     return max(res[0], res[1])


# if __name__ == '__main__':
#     arr = [2, 7, 9, 1, 10, 3]
#     arr = [1]
#     print(house_robber2(arr))
