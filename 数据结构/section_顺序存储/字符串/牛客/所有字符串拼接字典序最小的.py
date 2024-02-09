def process(str1, str2):
    if str1 + str2 > str2 + str1:
        return True
    else:
        return False


import functools


def process(strings):
    strings.sort(key=functools.cmp_to_key(process))
    print(strings)


if __name__ == '__main__':
    str1 = ['de', 'abc']
    print(process(str1))
