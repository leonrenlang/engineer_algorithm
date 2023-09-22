"""
问题：一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲。
给你每一个项目开始的时间和结束的时间，要求会议室进行的宣讲的场次最多
"""


# 思想：每次选择最早结束的项目，去掉因为做该项目不能做的项目
# 按照“结束时间”排序。设当前会议室被占用时间到0点，遍历排好序的项目
# 如果该项目的开始时间大于被占用时间，按照，更新被占用时间。
def best_arrange(programs):
    programs.sort(key=lambda program: program[1])
    cur = 0
    res = 0
    for program in programs:
        if cur <= program[0]:
            cur = program[1]
            res += 1
    return res


# 可用于解决其他问题：
# 435：给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
def eraseOverlapIntervals(intervals):
    import sys
    intervals.sort(key=lambda interval: interval[1])
    cur = -sys.maxsize
    res = 0
    for interval in intervals:
        if cur <= interval[0]:
            res += 1
            cur = interval[1]
    return len(intervals) - res


# 452. 用最少数量的箭引爆气球
# 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。
# 由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。
# 平面内最多存在104个气球。
#
# 一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，
# 若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。
# 可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

# 思想：
# - 最大的无重叠区间可知，如果最多有n个不重叠区间，那么最多需要n个箭头穿透所有区间
def findMinArrowShots(points):
    import sys
    programs = points
    programs.sort(key=lambda program: program[1])
    cur = -sys.maxsize
    res = 0
    for program in programs:
        if cur < program[0]:
            cur = program[1]
            res += 1
    return res


if __name__ == "__main__":
    programs = [(1, 7), (4, 8), (3, 6), (9, 19), (9, 11), (11, 13)]
    print(best_arrange(programs))
