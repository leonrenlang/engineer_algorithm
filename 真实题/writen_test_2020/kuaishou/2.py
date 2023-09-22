
original_num = 984561612
num = [int(item) for item in str(original_num)]
add_dic = {0:8, 1:7, 3:9, 5:9, 6:8}
delete_dic = {7:1, 8:6, 9:5}
action_flag = False

#找减掉一根的
idx = len(num) - 1
while idx >= 0:
    if num[idx] in delete_dic.keys():
        num[idx] = delete_dic[num[idx]]
        action_flag = True
        break
    
    idx -= 1
#找能增加的
if action_flag:
    idx = 0
    while idx < len(num):
        if num[idx] in add_dic.keys():
            num[idx] = add_dic[num[idx]]
            action_flag = False
            break
        idx += 1
res = int(''.join([str(item) for item in num]))

if res == original_num or action_flag == True:
    print(-1)
else:
    print(res)