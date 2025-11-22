s = list(input())
cont = 0
for e in s:
    if e == list('hello')[cont]:
        cont += 1
    if cont == 5:
        print('YES')
        break
if cont != 5:
    print('NO')
