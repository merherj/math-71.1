start = input()
n = int(input())

x = int(start.split()[1])

for _ in range(n):
    op, y = input().split()
    y = int(y)
    if op == "FINISH":
        x -= y
    else:
        x += y

print(x)