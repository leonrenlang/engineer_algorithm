# 问题: 你面前有一栋从1到N共N层的楼，然后给你K个鸡蛋（k至少为1)
# - 现在确定这栋楼存在楼层0 <= F <= N,在这层楼将鸡蛋扔下去，鸡蛋恰好
# 没摔碎（高于F的楼层都会碎，低于F的楼层都不会碎）。
# - 问你，最坏情况下，你至少要扔几次鸡蛋，才能确定这个楼层F呢？


# 思路：
# - 如果鸡蛋个数是无限的，那么直接二分,最坏情况下至少要扔log(N)次；
# 如果鸡蛋个数只有一个，那么只能从一楼依次上楼扔，最坏情况下需要N次，但是
# 鸡蛋个数不确定，因此这两种思想都不可

# - 状态变量: 鸡蛋数K, 楼层N
# - 转移方程:
# 对于楼层数N: 我可以在任意楼层扔鸡蛋，因此dp[K, N] = min(dp[K, i]) for i in N
# 对于给定的楼层i: dp[k][i] = max(dp[k-1][i-1], dp[k][N-i]) + 1 for k in K for i in N
# - base case: 如果只有一个鸡蛋（K=1)， 只能线性扫描
# 如果楼层数为0， 不用扔鸡蛋
# https://mp.weixin.qq.com/s/xn4LjWfaKTPQeCXR0qDqZg


# 备忘录解法
def egg_drop(K, N):
    memo = {}

    def process(K, N):
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]
        res = float('INF')
        for i in range(1, N + 1):
            res = min(res,
                      max(process(K, N - i),
                          process(K - 1, i - 1)
                          ) + 1
                      )
        memo[(K, N)] = res
        return res

    return process(K, N)


# 用二分查找优化上述方法
# # https://leetcode-cn.com/problems/super-egg-drop/
def superEggDrop(self, K: int, N: int) -> int:
    memo = dict()

    def dp(K, N):
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]

        # for 1 <= i <= N:
        #     res = min(res,
        #             max(
        #                 dp(K - 1, i - 1),
        #                 dp(K, N - i)
        #                 ) + 1
        #             )

        res = float('INF')
        # 用二分搜索代替线性搜索
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1)  # 碎
            not_broken = dp(K, N - mid)  # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        memo[(K, N)] = res
        return res

    return dp(K, N)

# 动态规划进一步优化
pass
