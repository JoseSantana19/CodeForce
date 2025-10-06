n = int(input())
answers = input().split()
output = 'EASY'
for e in range(n):
    if answers[e] == '1':
        output = 'HARD'
        break
print(output)
