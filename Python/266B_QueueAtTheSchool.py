n, t = map(int, input().split())
s = list(input())
for _ in range(t):
    cont = 0
    while cont < n - 1:
        if s[cont] == 'B' and s[cont+1] == 'G':
            s[cont] = 'G'
            s[cont+1] = 'B'
            cont += 1
        cont += 1
print("".join(s))
