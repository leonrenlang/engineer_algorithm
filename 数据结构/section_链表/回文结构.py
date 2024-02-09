"""  
判断一个链表是否为回文结构
【题目】 给定一个链表的头节点head，请判断该链表是否为回
文结构。 例如： 1->2->1，返回true。 1->2->2->1，返回true。
15->6->15，返回true。 1->2->3，返回false。
进阶： 如果链表长度为N，时间复杂度达到O(N)，额外空间复杂
度达到O(1)。

"""


# 用一个栈保存，如果一个链表和其逆序结果相同，则是回文结构
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def isPalindrome(head: ListNode) -> bool:
    if head == None:
        return True
    val_list = []
    while head:
        val_list.append(head.val)
        head = head.next
    reverse_list = val_list[::-1]
    return True if reverse_list == val_list else False


# 两个指针，找到中间节点，后半段入栈，栈与前半段比较
def is_palindrome2(head):
    if not head or not head.next:
        return True
    slow = head.next  # 找到中间节点，正常slow应该从head开始，但是中间节点不用判断，因此后面需要用其next
    fast = head  # 就直接再这里先next一下
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    stack = []  # 进栈
    while slow:
        stack.append(slow)
        slow = slow.next
    p1 = head  # 出栈比较
    while stack:
        if p1.val != stack.pop().val:
            return False
        p1 = p1.next
    return True


# **了解思路，不用看代码
# 两个指针，找到中间节点，将链表后半段逆序
# 一个指针从头，一个指针从尾，向中间移动，直到中间都相等，那么为回文链表，否则不是。
#  将链表的结构改回去

def is_palindrome3(head):
    if not head or not head.next:
        return True

    slow, fast = head, head
    while fast.next and fast.next.next:  # 为什么判断fast.next,因为如果fast.next不存在，则fast.next.next会报错
        slow = slow.next
        fast = fast.next.next

    right = slow.next  # 反转链表
    slow.next = None
    behind = None
    pre = slow
    while right:
        behind = right.next
        right.next = pre
        pre = right
        right = behind

    end = pre
    p1 = head
    res = True
    while p1 and pre:
        if p1.val != pre.val:
            res = False
            break
        p1 = p1.next
        pre = pre.next

    pre = None  # 将链表重新翻过来
    behind = None
    while end:
        behind = end.next
        end.next = pre
        pre = end
        end = next
    slow.next = pre
    return res
