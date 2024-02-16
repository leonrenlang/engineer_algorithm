
n = int(input())
start_arr = list(map(int, input().strip().split(' ')))
end_arr = list(map(int, input().strip().split(' ')))


start_trans = [0] * (n + 1)
for idx in range(1, n+1):
    start_trans[start_arr[idx-1]] = idx
end_trans = [0] * (n+1)
for idx in range(1, n+1):
    end_trans[end_arr[idx-1]] = idx

count = 0
for idx in range(2, n+1):
    cur_num = start_trans[idx]
    for j in range(1,idx):
        index_cur = end_trans.index(cur_num)
        if index_cur >= idx:
            break
        if start_trans[j] in end_trans[index_cur+1:]:
            count += 1
            break

print(count)
