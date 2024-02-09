

""" 作用
    检查两个元素是否属于同一个集合
    两个元素各自所在的集合，把他们集合到一起
    不能针对流来进行处理
思想：
    如果使用链表实现，判断需要遍历O(n)，合在一个O(1)；如果使用hash表，检查O(1),合并O(n)
    只要查询次数+合并次数逼近了O(n)以上，查询和合并和平均复杂度是O(1) """
class Node:
    def __init__(self):
        pass

class union_find_set:
    def __init__(self, nodes):
        self.father_map = {}
        self.size_map = {}
        for node in nodes:
            self.father_map[node] = node
            self.size_map[node] = 1
    
    def find_head(self, node):
        # 找到每个节点所在的集合的头，然后把沿途的所有节点直接连向头
        father = self.father_map[node]
        if father != node:
            father = self.find_head(father)
        self.father_map[node] = father
        return father
    
    def is_same_set(self, node1, node2):
        return self.father_map[node1] == self.father_map[node2]

    def union(self, node1, node2):
        if not node1 or not node2: return None
        a_head = self.find_head(node1)
        b_head = self.find_head(node2)
        if a_head != b_head:
            a_setsize = self.size_map[a_head]
            b_setsize = self.size_map[b_head]
            if a_setsize <= b_setsize:
                self.father_map[a_head] = b_head
                self.size_map[b_head] = (a_setsize + b_setsize)
            else:
                self.father_map[b_head] = a_head
                self.size_map[a_head] = (a_setsize + b_setsize)