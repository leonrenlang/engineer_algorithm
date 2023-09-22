
def judge_two_obj(lis1,lis2):
    lis = [item1 + item2 for item1, item2 in zip(lis1, lis2)]
    if min(lis) == max(lis):
        return 1
    else:
        return 0 
n, k = list(map(int, input().split()))
obj_lis = []
for _ in range(n):
    obj_lis.append(list(map(int, input().split())))
count = 0
for i in range(len(obj_lis)):
    for j in range(i+1, len(obj_lis)):
        count += judge_two_obj(obj_lis[i], obj_lis[j])
print(count)

