
"""  
设计RandomPool结构
【题目】 设计一种结构，在该结构中有如下三个功能：
insert(key)：将某个key加入到该结构，做到不重复加入O(1)。
delete(key)：将原本在结构中的某个key移除O(1)。 
getRandom()：严格等概率随机返回结构中的任何一个keyO(1)。
"""

# 思路：
# 其实就是给哈希表增加一个可以等概率随机返回一个值功能

import random
class RandomPool:
    def __init__(self):
        self.map1 = {}
        self.map2 = {}
        self.size = 0
    def add(self, key):
        if key not in self.map1.keys():
            self.map1[key] = self.size
            self.map2[self.size] = key
            self.size += 1

    def get_random(self):
        if self.size == 0:
            return None
        index = int(random.random() * self.size)
        return self.map2[index]

    def delete(self, key):
        if key in self.map1.keys():

            index = self.map1[key]       # 取信息
            self.size -= 1
            last_index = self.size
            last_key = self.map2[last_index]

            self.map1[last_key] = index  #更新需要保留的信息
            self.map2[index] = last_key   # 删除多余信息
            self.map1.pop(key)
            self.map2.pop(last_index)

