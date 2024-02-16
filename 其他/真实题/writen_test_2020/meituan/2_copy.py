
n = int(input())
start_arr = list(map(int, input().strip().split(' ')))
end_arr = list(map(int, input().strip().split(' ')))


count = 0
for i in range(len(start_arr)):
    if start_arr[i] < end_arr[i]:
        count += 1
print(count)