t = int(input())
for e in range(t):
    x, n = list(map(int, input().split()))
    if n % 2 == 1:
        print(x)
    else:
        print(0)
