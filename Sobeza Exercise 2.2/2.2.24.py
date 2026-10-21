n, h, k = [int(x) for x in input().split()]

md = 0
for _ in range(n):
    x, y = [int(v) for v in input().split()]
    d2 = (x - h) ** 2 + (y - k) ** 2
    if d2 > md:
        md = d2

r = md ** 0.5
d = r * 2

print(f"{d:.4f}")