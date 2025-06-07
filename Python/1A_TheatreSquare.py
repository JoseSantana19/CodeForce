import math

n, m, a = list(map(lambda x : int(x), input().split()))
print(math.ceil(n/a) * math.ceil(m/a) )
