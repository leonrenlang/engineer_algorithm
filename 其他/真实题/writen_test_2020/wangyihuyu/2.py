
def total_possibility(list1, list2):
    if len(list1) == 1 & len(list2) == 1:
        return 1
    small = list1[0]
    count = 0
    for idx in range(len(list2)):
        if small >= list2[idx]:
            new_list1 = list1[1:]
            new_list2 = list2[:idx] + list2[idx+1:]
            count += total_possibility(new_list1, new_list2)
    return count
n = input().strip()
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list1.sort()
list2.sort()
m = int(input().strip())
print(total_possibility(list1, list2) % m)