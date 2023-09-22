

n = 10
k = 3
n, k = list(map(int,input().strip().split(' ')))
def sum_bug(x, k):
    total = x
    power = 1
    while x // pow(k,power) != 0:
        total += x // pow(k,power)
        power += 1
    return total
x = 1
flag = False
while not flag:
    total = sum_bug(x, k)
    if total >= n:
        print(x)
        break
    else:
        x += 1
