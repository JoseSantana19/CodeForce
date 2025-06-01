n = int(input())
solutions = 0
for e in range(n):
    resp = input().split()
    count = 0
    for j in resp:
        if j == '1':
            count += 1
    if count >= 2:
        solutions += 1
print(solutions)
