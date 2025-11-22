n = int(input())
cont = 0
for e in range(n):
    inp = input().split()
    p, q = int(inp[0]), int(inp[1])
    if q - p >= 2:
        cont += 1
print(cont)
