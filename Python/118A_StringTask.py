vowels = ["a", "o", "y", "e", "u", "i"]
string = list(input().lower())
output = ""
for e in string:
    if e not in vowels:
        output += "." + e
print(output)
