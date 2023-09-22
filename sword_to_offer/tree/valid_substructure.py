

# 判断B是不是A的子结构，如果B不存在，则认为不是
# 遍历A,对于A的每一个节点，判断是不是子结构

def isSubStructure(A, B):
    def recur(A, B):
        if not B: return True
        if not A or A.val != B.val: return False
        return recur(A.left, B.left) and recur(A.right, B.right)
    return recur(A,B) or isSubStructure(A.left, B) or isSubStructure(A.right, B) if A and B else False

