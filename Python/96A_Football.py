cont = 0
players = input()
output = 'NO'
for e in range(len(players)-6):
    if players[e:e+7] == '1111111' or players[e:e+7] == '0000000':
        output = 'YES'
        break
print(output)
