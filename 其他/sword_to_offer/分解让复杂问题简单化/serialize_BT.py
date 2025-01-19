
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 序列化与反序列化二叉树
# 使用先序搜索，遇到空设置为特殊符号
class Codec:
    def serialize(self, root):
        # 这里之所以要定义一个辅助函数是因为：
        # 1.需要一个全局变量
        # 2. 需要等所有子递归函数运行完再返回
        if not root:  return []
        result = []
        def encodes(root):
            if not root:
                result.append('$')
                return None
            result.append(root.val)
            encodes(root.left)
            encodes(root.right)
        encodes(root)
        return result
    def deserialize(self, data):
        # 这里之所以定义一个辅助函数，因为在这里判断data是否存在能加快速度
        # 将index定义为self.index可不适用辅助函数
        if not data: return None
        index = [0]     #有地址的变量
        def decodes(data):
            if data[index[0]] == '$':
                index[0] += 1
                return None
            node = TreeNode(data[index[0]])
            index[0] += 1
            node.left = decodes(data)   #因为有占位符，左子树造完了自动开始造右子树
            node.right = decodes(data)
            return node
        return decodes(data)

