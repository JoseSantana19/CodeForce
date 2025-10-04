anton, danik = 0, 0
n = int(input())
s  = input()
for e in range(n):
    if s[e] == 'A':
        anton += 1
    elif s[e] == 'D':
        danik += 1
if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else:
    print('Friendship')
