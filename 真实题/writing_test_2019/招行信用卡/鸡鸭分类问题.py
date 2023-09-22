# 问题:用一个字符串表示一个鸡鸭队伍，要求以最小的代价将鸡鸭队伍分成两个部分
# 每次只能交换相邻的一对鸡鸭，问最少要交换多少次、


# 思想：
# - 交换有两种可能，鸡在左鸭在右，或者反之，输出两者中较小的即可。
# - 以鸡在左为例，要想将所有的鸡都换到左边，可能有许多种换法，只要每次将一组逆序的鸡鸭
# 矫正，进行的步骤数都应该是一样的。那么要怎么快速的求得这个步骤数呢？
# 获取所有鸡的初始下标，减去全部换完之后的下标，就是需要的步骤。
def process(string):
    chicken_axis = [i for i in range(len(string)) if string[i] == 'C']
    duck_axis = [i for i in range(len(string)) if string[i] == 'D']
    chicken_left = sum(chicken_axis) - sum(list(range(0, len(chicken_axis))))
    duck_left = sum(duck_axis) - sum(list(range(0, len(duck_axis))))
    print(min(chicken_left, duck_left))



if __name__ == '__main__':
    string = input()
    process(string)
