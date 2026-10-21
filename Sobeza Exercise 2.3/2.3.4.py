n = int(input())
c = [int(v) for v in input().split()]
t = int(input())

for _ in range(t):
    x, d = input().split()
    x = int(x) -1

    if d == "RIGHT":
        target = (x - 1) % n 
    else:
        target = (x + n // 2) % n

    half = c[x] // 2
    c[x] -= half
    c[target] += half

print(*c)