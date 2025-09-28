n, k = list(map(int, input().split()))
lista = list(map(int, input().split()))
cont = 0
for e in range(n):
    if e == 0:
        if lista[e] > 0:
            cont = 1
        else:
            break
    else:
        if lista[e] != 0:
            if e < k or (lista[e] == lista[e - 1]):
                cont += 1
            else:
                break
        else:
            break
print(cont)
