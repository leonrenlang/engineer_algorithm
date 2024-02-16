
k = 2
n = 100
lis = [1] * (k)
lis.append(k)
for _ in range(n-(k+1)):
    lis.append(lis[-1]*2 - lis[-(1+k)])
    lis.pop(0)
print(lis[-1] % 397)

