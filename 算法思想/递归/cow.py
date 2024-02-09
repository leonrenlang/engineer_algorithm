# 题目：母牛每年生一只母牛，新出生的母牛成长三年后也能每年生一直母牛
# 假设牛不会死，求N年后，母牛的数量


# 思想：F(n) = F(n-1) + F(n-3)
# 今年的牛的数量 = 去年牛的数量F(n-1) + 新生牛的数量（三年前的牛都可以生F(n-3))

def num_cow(n):
    # N是年份
    if n == 1 or n == 2 or n == 3:
        return n
    return num_cow(n - 1) + num_cow(n - 3)


if __name__ == '__main__':
    print(num_cow(6))
