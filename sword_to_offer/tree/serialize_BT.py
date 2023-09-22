

# 序列化与反序列化二叉树
# 使用先序搜索，遇到空设置为&就不用中序也能反序列化

def serialize(root):

    if not root:
        return []
    result = []
    def encodes(root):
        if not root:
            result.append('$')
            return
        result.append(root.val)
        encodes(root.left)
        encodes(root.right)
    encodes(root)
    return result

def deserialize(data):

    if not data:
        return []
    index = [0]
    def decodes(data):
        if data[index[0]] == '$':
            index[0] += 1
            return None
        node = TreeNode(data[index[0]])
        index[0] += 1
        node.left = decodes(data)
        node.right = decodes(data)
    return decodes(data)