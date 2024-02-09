# 组合问题: 输入两个数字, n, k
# n代表一个内容为1到n的数组，k代表要从数组中选取k个元素，输出所有可能的组合

# 更符合直觉的写法
def combination(n, k):
    def backtrack(n, i, track):
        if i == n + 1:
            if len(track) == k:
                res.append(track[:])
            return
        track.append(i)
        backtrack(n, i + 1, track)
        track.remove(i)
        backtrack(n, i + 1, track)

    res = []
    backtrack(n, 1, [])
    return res


if __name__ == '__main__':
    n = 4
    k = 2
    print(combination(4, 2))
