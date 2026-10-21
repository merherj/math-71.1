n = int(input())
bits = input()

new = []
for i in range(n):
    if i == 0 or bits[i] != bits[i - 1]:
        new.append(bits[i])

print("".join(new))