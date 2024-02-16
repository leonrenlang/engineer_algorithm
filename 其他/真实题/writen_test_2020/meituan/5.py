
n, k = list(map(int, input().strip().split(' ')))
str_arr = []
for i in range(k):
    str_arr.append(input().strip())
cal_str_arr = str_arr[:]

def cal_match(item, long_str):
    count = 0
    for idx in range(len(long_str) - len(item) + 1):
        if long_str[idx:idx + len(item)] == item:
            count += 1
    return count

for _ in range(n):
    input_str = input().strip()
    if input_str[0] == '?':
        long_str = input_str[1:]
        count = 0
        for item in cal_str_arr:
            if not item == '|':
                count += cal_match(item, long_str)
        print(count)
    elif input_str[0] == '+':
        index = int(input_str[1:]) - 1 
        if cal_str_arr[index] == '|':
            cal_str_arr[index] = str_arr[index]
    elif input_str[0] == '-':
        index = int(input_str[1:]) - 1
        cal_str_arr[index] = '|'



