n = int(input())
div = 4
divisao_quase_da_sorte = False
while div <= n:
    numero_da_sorte = True
    for e in str(div):
        if e != '4' and e != '7':
            numero_da_sorte = False
            break
    if numero_da_sorte and n % div == 0:
        divisao_quase_da_sorte = True
        break
    div += 1
if divisao_quase_da_sorte:
    print('YES')
else:
    print('NO')
