
# a, b = list(map(int, input().split()))
a = 2
b = 5

num_str = ''
for idx in range(1, a):
    num_str += str(idx)

count = 0
for idx in range(a, b+1):
    num_str += str(idx)
    sum = 0
    for char in num_str:
        sum += int(char)
    if sum % 3 == 0:
        count += 1
print(count)
