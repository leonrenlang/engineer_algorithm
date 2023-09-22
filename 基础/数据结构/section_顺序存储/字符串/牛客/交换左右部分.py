# 给定一个字符串，和一个整数，i代表str中的位置
# 将str[0..i]移到右侧，str[i+1, N-1]移到左侧

def reverse_part(string, i, j):
    while i < j:
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1


def process(string, i):
    string = list(string)
    reverse_part(string, 0, i)
    reverse_part(string, i + 1, len(string) - 1)
    reverse_part(string, 0, len(string) - 1)
    return ''.join(string)


if __name__ == '__main__':
    string = 'ABCDE'
    i = 2
    print(process(string, i))
