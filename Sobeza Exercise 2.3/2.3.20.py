m, n = [int(x) for x in input().split()]

secret = [0]

i = 0
while i < n:
    u, v = [int(x) for x in input().split()]

    if u in secret and v not in secret:
        secret.append(v)
    elif v in secret and u not in secret:
        secret.append(u)

    i += 1

print(len(secret))