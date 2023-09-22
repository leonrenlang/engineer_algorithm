class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 二叉树中和为某一值的路径
'''
对于某一个结点，如果我不存在，那么直接跳过。
如果我存在，把我塞进去试试，如果我没有孩子，那是一种结果
然后分别在我的孩子里面找。
找完后把我从路径中扔出来，因为我的孩子需要我，但我的兄弟不需要我
'''

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list[list[int]]:
        ans, path = [],[]
        def dfs(root, sum):
            if not root: return
            path.append(root.val)
            sum -= root.val
            if not root.left and not root.right and not sum:
                ans.append(path[:])
            dfs(root.left, sum)
            dfs(root.right, sum)
            path.pop()
        
        dfs(root, sum)
        return ans
        

