def generateRandomArray(max_size, value_radius):
    # 返回一个size在[1, max_size]之间，值在[-max_value, max_value]之间的随机数组
    import random
    size = int(max_size * random.random() + 1)
    array = []
    for _ in range(size):
        array.append(random.randint(-1 * value_radius, value_radius))
    return array


def array_validator(correct_algorithm, test_algorithm, iter, max_size, value_radius):
    for _ in range(iter):
        array = generateRandomArray(max_size, value_radius)
        array2 = array[:]
        array3 = array[:]
        array2 = test_algorithm(array2)
        array3 = correct_algorithm(array3)
        if array2 != array3:
            print("错误样例")
            print('sample:', array)
            print('test_algorithm:', array2)
            print('correct_algorithm:', array3)
            exit()

    print('Algorithm pass!')
    array = generateRandomArray(max_size, value_radius)  # 算法通过，给出一个样例
    print(array)
    print(test_algorithm(array))


if __name__ == "__main__":
    from section1_sort_compare.sort_compare.O2_sort import correctSort
    from section1_sort_compare.sort_compare.heap_sort import heap_sort

    array_validator(iter=10000, max_size=5, value_radius=10,
                    correct_algorithm=correctSort,
                    test_algorithm=heap_sort)
