n, h = list(map(int, input().split()))
a = list(map(int, input().split()))
for e in a:
    if e > h:
        n += 1
print(n)
