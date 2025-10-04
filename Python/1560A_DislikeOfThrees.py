t = int(input())
for _ in range(t):
    k = int(input())
    cont = 0
    num = 0
    while cont < k:
        num += 1
        if num % 3 != 0 and num % 10 != 3:
            cont += 1
    print(num)
