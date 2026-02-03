x = input()
resp = 'NO'
for e in x:
    if e in ['H','Q','9']:
        resp = 'YES'
        break
print(resp)
