n = int(input())
maximo, numPassageiros = 0, 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    numPassageiros = numPassageiros - a + b
    if numPassageiros > maximo:
        maximo = numPassageiros
print(maximo)
