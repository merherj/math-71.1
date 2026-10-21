n = int(input())
h = [int(x) for x in input().split()]
Q = int(input())

for _ in range(Q):
    L, R = [int(x) for x in input().split()]

    s = sorted(h[L - 1:R])
    m = len(s)

    if m % 2 == 1:
        med = s[m // 2]
    else:
        med = (s[m // 2 - 1] + s[m // 2]) / 2

    print(f"{med:.2f}")