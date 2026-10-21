n = int(input())
a = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

cinv = [0] * n
j = 0
while j < n:
    cinv[c[j] - 1] = j + 1
    j += 1

b = [0] * n
i = 0
while i < n:
    b[a[i] - 1] = cinv[i]
    i += 1

print(*b)