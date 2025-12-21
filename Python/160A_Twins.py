n = int(input())
lista = sorted(list(map(int, input().split())), reverse=True)
for e in range(1,n+1):
    if sum(lista[0:e]) > sum(lista[e:]):
        break
print(e)
