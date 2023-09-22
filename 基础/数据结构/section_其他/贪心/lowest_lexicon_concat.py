import functools


# 问题：给定一堆字符串，求全部拼接结果字典序最小的字符串

# 思路：使用贪心策略，对所有字符串排序。
# 虽然结果是求最小的字典序，但是字符串两两比较不能简单的使用其各自的字典序，b和字典序小于ba，但是b应该放在ba后面。
# 因此对于两个字符串，如果（str1 拼接 str2）的字典序大于（str2 拼接 str1）,则认为str1应该放在str2后面


def my_comparator(str1, str2):
    concat1 = str1 + str2
    concat2 = str2 + str1
    if concat1 > concat2:  # python默认的字符串比较方式是按照其字典序进行比较
        return 1
    else:
        return -1


def lowest_lexicon_concat(lexicon):
    """  
    type lexicon: list[str]
    rtype res: str
    """
    lexicon_sorted = sorted(lexicon, key=functools.cmp_to_key(my_comparator))
    res = ''
    for item in lexicon_sorted:
        res += item
    return res


if __name__ == "__main__":
    str_array = ['ba', 'a', 'b']
    print(lowest_lexicon_concat(str_array))
