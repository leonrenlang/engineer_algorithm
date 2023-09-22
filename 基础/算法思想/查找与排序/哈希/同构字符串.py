# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
# 示例 1:
# 输入: s = "egg", t = "add"
# 输出: true
# 示例 2:
# 输入: s = "foo", t = "bar"
# 输出: false
# 示例 3:
# 输入: s = "paper", t = "title"
# 输出: true

'''
    思想: 
       遍历字符串长度，两个set分别保存两个字符串中的字符，用于判断是否出现过，他们必须同时存在出现过的字符，
       并且出现过的字符的映射应该是一致的

        一个map保存每个映射
'''

def is_isomorphic(s, t):
    '''
        s： base 字符串
        t： 判断字段串
    '''
    if len(s) != len(t): return False
    dic = {}
    seen = set()
    for idx in range(len(s)):
        if s[idx] in dic.keys():
            # 如果字符出现过，判断映射是否一致
            if dic[s[idx]] != t[idx]:
                return False
        else:
            if t[idx] in seen:
            # 如果base字符串没出现过，而判断字符串中当前字符出现过，不符合同构
                return False
            else:
            # 当前位置两个字符串的字符都为新增字符
                dic[s[idx]] = t[idx]
                seen.add(t[idx])
    return True


s = 'abba'
t = "dog cat cat cat"
print(is_isomorphic(s, t))
