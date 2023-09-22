
# 打印从1到最大的n位数
# 考虑数字超过整数能表示的范围的情况

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        def add_one(big_num):
            flag = 1
            index = -1
            while flag:
                if big_num[index] < 9:
                    big_num[index] += 1
                    flag = 0
                else:
                    big_num[index] = 0
                    index -= 1
        res = []
        big_num = [0] * n
        for _ in range(pow(10, n) - 1):
            add_one(big_num)
            res.append(int(''.join([str(item) for item in big_num])))
        return res