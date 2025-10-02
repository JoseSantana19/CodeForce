k, n, w = list(map(int, input().split()))
total = 0
for e in range(1,w+1):
    total += e * k
total = total - n
if total < 0:
    total = 0
print(total)
