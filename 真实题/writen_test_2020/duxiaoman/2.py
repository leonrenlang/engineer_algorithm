
# 1快钱能去吗
# 2快。。。。

N, A, B, C = list(map(int, input().split()))
aim_list = list(map(int, input().split()))
aim_dict = {key:value for key, value in zip(range(1, len(aim_list) + 1), aim_list)}



class ListNode:
    def __init__(self, left, mid, right):
        self.left = None
        self.mid = None
        self.right = None
node_set = []
for key,value in aim_dict.item():
    node_set.append(ListNode())
