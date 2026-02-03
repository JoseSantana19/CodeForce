n = int(input())
string = input().lower()
if len(set(string)) == 26:
    print('YES')
else:
    print('NO')
