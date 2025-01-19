

# 原地反转列表
# 保存三个指针，分别指向pre, cur, next
# 最后一次判断tmp为空的时候，还是要把cur.next指向pre再返回结果

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
            if not head: return None

            pre = None
            cur = head
            result = None
            while cur:
                tmp = cur.next
                if tmp == None:
                    result = cur
                cur.next = pre
                pre = cur
                cur = tmp
            return result