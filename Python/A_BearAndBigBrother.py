a, b = list(map(int, input().split()))
cont = 0
while a <= b:
    a *= 3
    b *= 2
    cont += 1
print(cont)
