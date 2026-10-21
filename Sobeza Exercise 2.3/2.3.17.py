n = int(input())
p = [int(x) for x in input().split()]

colors = [0] * n 

i = 0
while i < n:
    pos = p[i] - 1

    used = []
    if pos > 0:
        used.append(colors[pos - 1])
    if pos < n - 1:
        used.append(colors[pos + 1])

    c = 1
    while c in used:
        c += 1

    colors[pos] = c
    i += 1

print(*colors)