

""" 题目1：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student.
 "，则输出"student. a am I"。 """


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])


""" 题目2：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
该函数将返回左旋转两位得到的结果"cdefgab"。
 """
 
# 思路：整个字符串反转一次，然后0~len(s)-k转一次，len(s)-k:转一次
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        s = list(reversed(s))
        s[:(len(s)-n)] = list(reversed(s[:(len(s) - n)]))
        s[(len(s)-n):] = list(reversed(s[(len(s) - n):]))
        return ''.join(s)