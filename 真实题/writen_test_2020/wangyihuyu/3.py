

n, m = list(map(int, input().split()))
player = []
for _ in range(n):
    player.append(input().strip())

rules = []
input_str = input().strip()
while input_str != '0 0 N 0 0':
    rules.append(input_str.split())
    input_str = input().strip()

count = [0] * n
for rule in rules:
    if rule[2] == 'Y':
        count[int(rule[0])-1] += 1
        count[int(rule[3])-1] += 1
print(count)
print(rules)

