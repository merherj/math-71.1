n = int(input())

d = []
for _ in range(n):
    a, b = [int(v) for v in input().split()]
    d.append((a, b))

p = [d[0][0], d[0][1]]

for i in range(1, n):
    a, b = d[i]
    new = []
    for v in p:
        if v == a:
            if b not in new:
                new.append(b)
        if v == b:
            if a not in new:
                new.append(a)
    p = new

if len(p) == 0:
    print("NO")
else:
    print("YES")