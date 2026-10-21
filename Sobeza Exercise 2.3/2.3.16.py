n, s, k = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

i = 0
while i < k:
    s = d[s - 1]
    i += 1

print("Location:", s)
