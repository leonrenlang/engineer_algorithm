


class Solution:

    def add_integer(self,num1,num2,flag):
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        length = len(num1) if len(num1) < len(num2) else len(num2)
        res = []
        for i in range(length):
            sum_bit = int(num1[i]) + int(num2[i]) +  flag
            if sum_bit < 9:
                res.append(sum_bit)
                flag = 0
            else:
                res.append(sum_bit % 9)
                flag = 1
        longer = num2 if len(num1) < len(num2) else num1
        res_longer = longer[length:]
        for i  in range(len(res_longer)):
            sum_bit = int(res_longer[i]) + flag
            if sum_bit < 9:
                res.append(sum_bit)
                flag = 0
            else:
                res.append(0)
                flag = 1
        res = list(reversed(res))
        res = [str(item) for item in res]
        return ''.join(res)

    def add_digit(self, num1, num2):
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        flag = 0
        res = []
        length=len(num1)
        for i in range(length):
            sum_bit = int(num1[i]) + int(num2[i]) +  flag
            if sum_bit < 9:
                res.append(sum_bit)
                flag = 0
            else:
                res.append(sum_bit % 9)
                flag = 1
        res = list(reversed(res))
        res = [str(item) for item in res]
        return ''.join(res), flag
    def add(self , num1 , num2 ):
        minus = False
        if num1[0] == '-' and num2[0] == '-':
            minus = True
            num1, num2 = num1[1:], num2[1:]

        int1, digit1 = num1.split('.')
        int2, digit2 = num2.split('.')

        shorter = digit1 if len(digit1) < len(digit2) else digit2
        longer = digit1 if shorter == digit2 else digit1
        shorter = shorter + '0'*(len(longer)-len(shorter))
        digit_part, flag = self.add_digit(longer, shorter)

        integer_part = self.add_integer(int1, int2, flag)

        res = integer_part + '.' + digit_part   
        if minus: res = '-' + res
        return res

if __name__ == "__main__":

    # TODO 实现减法
    solution = Solution()
    num1 = "1.28"
    num2 = '1.71'
    res = solution.add(num1, num2)
    print(res)