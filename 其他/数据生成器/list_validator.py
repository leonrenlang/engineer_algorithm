import random


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def list_generator(max_size, value_radius):
    size = random.randint(1, max_size)
    head = Node(random.randint(-1 * value_radius, value_radius))
    tmp = head
    for _ in range(1, size):
        tmp.next = Node(random.randint(-1 * value_radius, value_radius))
        tmp = tmp.next
    return head


def list_print(head):
    p1 = head
    while p1:
        print(p1.val)
        p1 = p1.next


def copy_list(head):
    # 复制一个链表
    if not head: return None
    copy_head = Node(head.val)
    p1 = head.next
    copy_rear = copy_head
    while p1:
        node = Node(p1.val)
        copy_rear.next = node
        copy_rear = node
        p1 = p1.next
    return copy_head


def equal_list(lis1, lis2):
    if isinstance(lis1, Node):
        p1 = lis1
        p2 = lis2
        while p1 and p2:
            if p1.val != p2.val:
                return False  # 不相同，返回False
            p1 = p1.next
            p2 = p2.next
        return True
    else:
        return True if lis1 == lis2 else False

def list_validator(correct_algorithm, test_algorithm, iter, max_size, value_radius):
    for _ in range(iter):
        lis1 = list_generator(max_size, value_radius)
        lis2 = copy_list(lis1)
        lis3 = copy_list(lis1)
        lis2 = test_algorithm(lis2)
        lis3 = correct_algorithm(lis3)
        if not equal_list(lis2, lis3):
            print("错误样例")
            print('sample:', lis1)
            print('test_algorithm:', lis2)
            print('correct_algorithm:', lis3)
            exit()

    print('Algorithm pass!')
    lis = list_generator(max_size, value_radius)  # 算法通过，给出一个样例
    list_print(lis)
    print(test_algorithm(lis))


if __name__ == '__main__':
    # lis1 = list_generator(max_size=10, value_radius=100)
    # list_print(lis1)

    from section3_linear_structure.linklist.is_parlindrome import isPalindrome, is_palindrome2, is_palindrome3
    list_validator(isPalindrome, is_palindrome3, iter=10000, max_size=20, value_radius=20)
