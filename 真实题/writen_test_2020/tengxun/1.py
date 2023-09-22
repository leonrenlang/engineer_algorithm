
import math
n, m = list(map(int, input().split()))
pays = 0
incomes = 0
profit = []
for _ in range(n):
    blood, income = list(map(int, input().split()))
    pays += blood / m
    incomes += income
    profit.append(incomes - pays)
# print(profit)
print(int(max(profit)))