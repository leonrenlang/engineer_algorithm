# 题目：有三个杆，杆上有一堆圆盘，圆盘按从小到大顺序从上往下一次穿在其中一个杆中
# 求代价最小的方法，将杆上的圆盘移到另一个圆盘上
# 要求：只能小圆盘压在大圆盘上面，一次只能移动一个盘



# 思想：父问题如何分解为子问题？三个杆分别命名为：from to help
# 假设f(n-1)问题已经解决
# 1. 将1~n-1移到help上
# 2. 将n移到to上
# 3. 将1~n-1移到to上
# 时间复杂度O(2^n)

# 目前问题规模为N,所有的盘都在origin杆上
def process(N, origin, to, help):
    if N == 1:
        print("Move 1 from %s to %s" % (origin, to))
    else:
        process(N - 1, origin, help, to)
        print('Move %d from %s to %s' % (N, origin, to))
        process(N - 1, help, to, origin)


if __name__ == '__main__':
    process(3, "左", "中", "右")
