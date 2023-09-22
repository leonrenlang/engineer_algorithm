
def get_gap(lis):
    gap = []
    for idx in range(1, len(lis)):
        gap.append(lis[idx] - lis[idx-1])
    return str(gap)
def get_anti_pattern(pattern):
    lis = eval(pattern)
    anti_lis = [(-1)*item for item in lis]
    return str(anti_lis)

n, k = list(map(int, input().split()))
pattern_dic = {}
for _ in range(n):
    att_arr = list(map(int, input().split()))
    gap = get_gap(att_arr)
    if gap not in pattern_dic:
        pattern_dic[gap] = 1
    else:
        pattern_dic[gap] += 1
count = 0
for pattern, value in pattern_dic.items():
    anti_pattern = get_anti_pattern(pattern)
    if anti_pattern in pattern_dic.keys():
        count += value*pattern_dic[anti_pattern]      
print(count // 2)



