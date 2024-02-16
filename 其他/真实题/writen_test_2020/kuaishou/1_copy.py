

str1 = input().strip()
idx = 0
flag = True
while flag:
    tmp = idx + 1
    while tmp < len(str1) and str1[tmp] == str1[idx]:
        tmp += 1
    if (tmp - idx) >= 3:
        str1 = str1[:idx] + str1[tmp:]
        idx = 0
    else:
        idx += tmp
    if idx == len(str1):
        flag = False
print(str1)