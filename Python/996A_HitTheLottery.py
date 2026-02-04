n = int(input())
cont = 0
for nota in [100,20,10,5,1]:
    cont += n // nota
    n -= n // nota * nota
print(cont)
