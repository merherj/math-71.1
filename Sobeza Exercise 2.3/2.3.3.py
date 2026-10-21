n = int(input())
L = [input().split()]
e = int(input())

for _ in range(e):
    x, y = [int(x) for x in input().split()]
    L[x - 1], L[y - 1] = L[y - 1], L[x - 1]

print(*L)
