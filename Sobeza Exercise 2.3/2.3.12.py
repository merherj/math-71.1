n, m = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

votes = [0]*n

i = 0
while i < m:
    votes[b[i] - 1] += 1
    i += 1

print(*votes)
