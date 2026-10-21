n, m = [int(x) for x in input().split()]

friends = [0] * n

i = 0
while i < m:
    u, v = [int(x) for x in input().split()]
    u = u-1
    v = v-1

    friends[v] +=1
    friends[u] +=1

    i+=1

print(*friends)