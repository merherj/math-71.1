n, r = [int(v) for v in input().split()]
a = [int(v) for v in input().split()]

def A(x):
    best = abs(x - a[0])
    for i in a:
        d = abs(x - i)
        if d < best:
            best = d
    return best

total = 0
for k in range(r):
    left = A(k)
    right = A(k + 1)
    total = total + (left + right)

area = total // 2

print(area)