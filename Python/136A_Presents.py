n = int(input())
p = list(map(int, input().split()))
output = []
for e in range(1,n+1):
    index = 1
    for i in p:
        if i == e:
            output.append(str(index))
            break
        index += 1
print(" ".join(output))
