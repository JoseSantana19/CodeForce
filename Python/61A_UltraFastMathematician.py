n1 = input()
n2 = input()
resp = ''
for e in range(len(n1)):
    if n1[e] == n2[e]:
        resp += '0'
    else:
        resp += '1'
print(resp)
