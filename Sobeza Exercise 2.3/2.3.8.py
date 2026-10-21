n = int(input())
h = [int(x) for x in input().split()]
Q = int(input())

for _ in range(Q):
    L, R, k = [int(x) for x in input().split()]

    i = L - 1
    while i < R:
        if h[i] <= k:
            h[i] = k
        i += 1

print(*h)