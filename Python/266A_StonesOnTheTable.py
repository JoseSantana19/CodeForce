n = int(input())
s = list(input())
ind = 0
contador = 0
while ind < n:
    if ind == len(s) - 1:
        break
    if s[ind] == s[ind+1]:
        s.pop(ind+1)
        contador += 1
    else:
        ind += 1
print(contador)
