
# 前缀树的功能：
#   - 有一堆字符串
#   - 1. 是否有给定字符串？
#       给每个节点增加一个数据项，有几个字符串以该节点结尾
#   - 2. 有多少个字符串以给定字符串为前缀？
#       - 给每个节点增加一个数据项，每个节点被划过几次
#       - 是否有字符串以给定字符串开头的？
#           有0个字符串以给定字符串为前缀

# 前缀树建立：
#   1. 路建立在边上，不是建立在节点上


class TrieNode:
    def __init__(self):
        self.path = 0 # 有多少字符串到达过这个节点
        self.end = 0 #有多少个字符串以该节点结尾
        self.nexts = [None] * 26   # 这是路，假设只有小写字母，则最多可能存在26条路（可复用）
                                # 如果不止小写字母，可以采用hashmap
class TrieTree:

    def __init__(self):
        self.root = TrieNode()
         
    def insert(self, word):
        if not word: return 
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if node.nexts[index] == None:
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            node.path += 1
        node.end += 1

    def search(self, word):
        # 给定word出现过几次
        if not word: return 
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if node.nexts[index] == None:
                return 0
            node = node.nexts[index]
        return node.end
    
    def delete(self, word):
        if self.search(word) != 0:
            node = self.root
            for i in range(len(word)):
                index = ord(word[i]) - ord('a')
                node.nexts[index] -= 1
                if node.nexts[index].path == 0:
                    node.nexts[index] = None
                    return 
                node = node.nexts[index]
        node.end -= 1

    def prefix_num(self, pre):
        if not pre: return 
        node = self.root
        for i in range(len(pre)):
            index = ord(pre[i]) - ord('a')
            if node.nexts[index] == None:
                return 0
            node = node.nexts[index]
        return node.path


