n = int(input())
cont = 0
ultimo = ''
for e in range(n):
    entrada = input()
    if entrada != ultimo:
        cont += 1
    ultimo = entrada
print(cont)
