n = int(input())
h = [int(x) for x in input().split()]
Q = int(input())

for _ in range(Q):
    L, R = [int(x) for x in input().split()]
    print(max(h[L - 1:R]))