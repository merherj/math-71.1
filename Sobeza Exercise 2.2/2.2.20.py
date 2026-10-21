s = input()

total = int(s[0])

for i in range(1, len(s)):
    if i % 2 == 1:
        op = s[i]
        digit = int(s[i + 1])
        if op == "+":
            total += digit
        else:
            total -= digit

print(total)