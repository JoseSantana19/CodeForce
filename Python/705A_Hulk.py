n = int(input())
out = 'I hate'
for e in range(n - 1):
    if e % 2 == 0:
        out += ' that I love'
    else:
        out += ' that I hate'
out += ' it'
print(out)
