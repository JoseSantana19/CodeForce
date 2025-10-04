cont = 0
n = list(input())
for e in n:
    if e in ['4', '7']:
        cont += 1
if cont in [4,7]:
    print('YES')
else: print('NO')
