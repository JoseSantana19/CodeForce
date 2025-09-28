matrix = []
for e in range(5):
    matrix.append(input().split())
for linha in range(5):
    for coluna in range(5):
        if matrix[linha][coluna] == '1':
            print(abs(linha-2)+abs(coluna-2))
            break
