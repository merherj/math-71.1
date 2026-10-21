n = int(input())
x = [int(v) for v in input().split()]
c = [int(v) for v in input().split()]

c.sort()

possible = True
for i in range(n):
    if c[i] < x[i]:
        possible = False

if possible:
    print("YES")
else:
    print("NO")