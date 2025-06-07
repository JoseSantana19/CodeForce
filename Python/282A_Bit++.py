n = int(input())
x = 0
for e in range(n):
    statement = input()
    if statement == 'X++' or statement == '++X':
        x += 1
    elif statement == 'X--' or statement == '--X':
        x -= 1
print(x)
