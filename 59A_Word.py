s = input()
lst = list(s)
lower = 0
upper = 0
for e in lst:
    if e in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        lower += 1
    else:
        upper += 1
if lower >= upper:
    print(s.lower())
else:
    print(s.upper())
