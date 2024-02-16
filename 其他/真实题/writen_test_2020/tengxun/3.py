
import math

m, n =  2,3
total = math.pow(m, n)
no_conflick = m * pow(m-1, n-1) 
print(int(total - no_conflick) % 100003)



"""  
m, n = list(map(int, input().split()))
total = pow(m, n)
no_conflick = m * pow(m-1, n-1) 
print((total - no_conflick) % 100003)
"""