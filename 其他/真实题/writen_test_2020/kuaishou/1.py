import re
import string
# str1 = input().strip()
alphabet = string.printable[:-6]
print(alphabet)
flag = True
while flag:
    flag = False
    for item in alphabet:
        res = re.search(f'{item}+',str1)
        if res:
            left, right = res.span()
            if (right - left) >= 3:
                str1 = str1[:left] + str1[right:]
                flag = True
print(str1)