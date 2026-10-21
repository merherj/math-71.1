n = int(input())
h = [int(x) for x in input().split()]
Q = int(input())

for _ in range(Q):
    L, R = [int(x) for x in input().split()]

    i = L - 1
    while i < R:
        h[i] += 1
        i += 1

print(*h)